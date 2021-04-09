# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.cloud import bigquery
from flask import *
from google.auth.transport import requests
from google.cloud import datastore, storage
from google.cloud.storage import client

app = Flask(__name__)

@app.route('/one')
def one():
    bigquery_client = bigquery.Client()
    query = """
        SELECT time_ref as TIME_REF, SUM(CASE WHEN account='Imports' THEN value END) + SUM(CASE WHEN account='Exports' THEN value END) as VALUE FROM `chetan-r-project2.task_2_1.task2_1` group by time_ref order by VALUE desc LIMIT 10
        """
    result = bigquery_client.query(query)
    return render_template('one.html', results = result)

@app.route('/two')
def two():
    bigquery_client = bigquery.Client()
    query = """
        SELECT country_label as COUNTRY_LABEL, product_type as PRODUCT_TYPE, SUM(CASE WHEN account='Imports' THEN value END) - SUM(CASE WHEN account='Exports' THEN value END)AS TRADE_DEFICIENT_VALUE, status as STATUS
        FROM `chetan-r-project2.task_2_1.task2_1` LEFT JOIN `chetan-r-project2.task_2_1.country`
        USING(country_code)
        WHERE SUBSTRING(time_ref, 1, 4) IN ('2014', '2015', '2016')
        AND status='F' AND product_type = "Goods"
        GROUP BY country_label, product_type, status
        ORDER BY TRADE_DEFICIENT_VALUE DESC
        LIMIT 50
        """
    result = bigquery_client.query(query)
    return render_template('two.html', results = result)

@app.route('/three')
def three():
    bigquery_client = bigquery.Client()
    query = """
        SELECT service_label as SERVICE_LABEL, SUM(CASE WHEN account='Exports' THEN value END) - SUM(CASE WHEN account='Imports' THEN value END)AS TRADE_SURPLUS_VALUE
FROM `chetan-r-project2.task_2_1.task2_1` LEFT JOIN `chetan-r-project2.task_2_1.serivce` on code = service_code
WHERE country_code in (SELECT country_code
        FROM `chetan-r-project2.task_2_1.task2_1` LEFT JOIN `chetan-r-project2.task_2_1.country`
        USING(country_code)
        WHERE SUBSTRING(time_ref, 1, 4) IN ('2014', '2015', '2016')
        AND status='F' AND product_type = "Goods"
        GROUP BY country_code, product_type, status
        LIMIT 50)
GROUP BY SERVICE_LABEL    
ORDER BY TRADE_SURPLUS_VALUE DESC
        LIMIT 30 
        """
    result = bigquery_client.query(query)
    return render_template('three.html', results = result)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
