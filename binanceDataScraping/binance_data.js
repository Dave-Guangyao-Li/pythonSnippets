// import binance_bracket_data.json

const binanceData = require('./binance_bracket_data.json');

// show contents of binanceData
const bracketsData = binanceData.data.brackets;
// console.log(bracketsData);

// reduce riskBrackets data inside bracketsData along with symbol
const reducedRiskBracketsData = bracketsData.reduce((acc, bracket) => {
    return {
        ...acc,
        [bracket.symbol]: [...bracket.riskBrackets].map((row) => {
            return {
                tier: row.bracketSeq,
                position_bracket: `${row.bracketNotionalFloor} - ${row.bracketNotionalCap}`,
                max_leverage: `${row.maxOpenPosLeverage}x`,
                maintenance_margin_rate: row.bracketMaintenanceMarginRate,
                maintenance_amount: row.cumFastMaintenanceAmount
            };
        })
    };
}, {});
console.log(reducedRiskBracketsData.CTSIUSDT.length);
// convert to JSON format and export reducedRiskBracketsData
const reducedRiskBracketsDataJSON = JSON.stringify(reducedRiskBracketsData);
// dump into JSON file 
const fs = require('fs');
fs.writeFileSync('reducedRiskBracketsData.json', reducedRiskBracketsDataJSON);



