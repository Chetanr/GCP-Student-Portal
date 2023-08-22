import { extractFromUrl, extractAndConvertToJson } from "./parser";

export const fileExtracter = async (url: string) => {
  extractFromUrl(url, "./extracts/");
  extractAndConvertToJson();
};
