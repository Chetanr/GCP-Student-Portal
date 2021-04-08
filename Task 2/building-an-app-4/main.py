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
        SELECT time_ref as TIME_REF, sum(value) as VALUE FROM `chetan-r-project2.task_2_1.task2_1` group by time_ref order by VALUE desc LIMIT 10
        """
    result = bigquery_client.query(query)
    return render_template('one.html', results = result)

@app.route('/two')
def two():
    bigquery_client = bigquery.Client()
    query = """
        SELECT t2.country_label AS COUNTRY_LABEL,t1.product_type AS PRODUCT_TYPE,(t1.value - t3.value) AS TRADE_DEFICIENT_VALUE, t1.status AS STATUS
FROM `chetan-r-project2.task_2_1.task2_1` AS t1, `chetan-r-project2.task_2_1.country` AS t2,`chetan-r-project2.task_2_1.task2_1` AS t3
JOIN
  t3 ON t1.time_ref = t3.time_ref
JOIN
  t2 ON t1.country_code = t2.country_code AND t3.country_code = t2.country_code
WHERE
  t3.account = 'Exports' AND t1.account = 'Imports' AND t1.status = 'F'
GROUP BY
  COUNTRY_LABEL,PRODUCT_TYPE,TRADE_DEFICIENT_VALUE,STATUS
ORDER BY
  TRADE_DEFICIENT_VALUE DESC
LIMIT
  50
        """
    result = bigquery_client.query(query)
    return render_template('two.html', results = result)

@app.route('/three')
def three():
    bigquery_client = bigquery.Client()
    query = """
        SELECT time_ref as TIME_REF, sum(value) as VALUE FROM `chetan-r-project2.task_2_1.task2_1` group by time_ref order by VALUE desc LIMIT 10
        """
    result = bigquery_client.query(query)
    return render_template('three.html', results = result)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
