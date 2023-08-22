import { request } from "http";
import decompress from "decompress";
import { createWriteStream, readdir, writeFile } from "fs";
import csv from "csvtojson";
import path from "path";

export const extractFromUrl = (url: string, location: string) => {
  request(url)
    .pipe(createWriteStream(location))
    .on("close", function () {
      console.log("File has been written!");
    });
};

export const extractAndConvertToJson = async () => {
  readdir("./extracts/", (err, files) => {
    for (const file of files) {
      if (path.extname(file) === ".zip") {
        const fileNameWithExtension = path.basename(file);

        decompress(file, `/extracts/${fileNameWithExtension}`);

        const fileNameWithoutExtension = path.parse(fileNameWithExtension).name;
        convertToJson(
          `/extracts/${fileNameWithExtension}`,
          fileNameWithoutExtension
        );
      }
    }
  });
};

export const convertToJson = (filepath: string, fileName: string) => {
  csv()
    .fromFile(filepath)
    .then((jsonArrayObj) => {
      writeFile(`${fileName}.json`, JSON.stringify(jsonArrayObj), (error) => {
        if (error) throw error;
        console.log("complete");
      });
    });
};
