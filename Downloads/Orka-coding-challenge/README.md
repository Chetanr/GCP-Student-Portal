# Application-engineer-code-challenge

You will be joining our engineering team whose focus will primarily involve building backend apps for the utilities domain.

## Scope of the challenge
The challenge is written in a way for you complete this in one evening or over a few hours on a weekend. Having said that, there is no time limit. Also, the challenge is not an exam and there is no pass or fail.

What matters to us is to learn how you write code and documentation, what you consider as clean code, and how you generally approach the problem given limited requirements. For us, it is more important to have an understandable project than a complex algorithm.

## Pre-requisite
- git
- Node.js >=v 18.0
- Typescript
- vitest for unit testing but Jest is ok too

PS: We have included a starter template you are allowed to over-ride this. We recommend you don't use any frameworks like NEST or express and keep it simple.

## Context
The Electricity meter reads in Australia as shared among australian companies in a format cadd NEM13 and NEM12. The documentation of the file format is maintained by AEMO at https://aemo.com.au/-/media/files/electricity/nem/retail_and_metering/market_settlement_and_transfer_solutions/2022/mdff-specification-nem12-nem13-v25.pdf?la=en

## Requirements
Write a library that can parse and validate the NEM12 and NEM13 files. Write the output to a SQlite DB or as JSON outputs per file.

The following is expected:
1. Upon successful file validation
2. parse the file and store the records with the source of the file
3. run validation against each record in item 2 and show either passed or failed validation
4. where validation failed show the error reason.

AEMO also publish test files for validation purpose which can be found below
- [NEM12 Example files](https://aemo.com.au/-/media/files/electricity/nem/retail_and_metering/metering-procedures/2016/nem12-example-files.zip)
- [NEM13 Example files](https://aemo.com.au/-/media/files/electricity/nem/retail_and_metering/metering-procedures/2016/nem13-example-files.zip)
- [NEM12 Error files](https://aemo.com.au/-/media/files/electricity/nem/retail_and_metering/metering-procedures/2016/nem12-error-files.zip)
- [NEM13 Error files](https://aemo.com.au/-/media/files/electricity/nem/retail_and_metering/metering-procedures/2016/nem13-error-files.zip)

If you need any more AEMO Documentation [here](https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/market-operations/retail-and-metering/metering-procedures-guidelines-and-processes)

Hints:
1. You may need to merge or group records in NEM12 before validation

Please include unit tests and you git commit history.

## Delivery of your solution

Please deliver your solution as a git repository in a ZIP file. The repository should contain full instructions for us to run the solution on our machines.

Also don't forget to include any more details that you think will help us understand your thought process better in the README.

One Final Request PLEASE DO NOT HOST YOUR SOLUTION IN A PUBLIC REPO.