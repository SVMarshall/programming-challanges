// https://leetcode.com/problems/excel-sheet-column-number/

/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function(s) {
    var value = 1; 
    var col = 0; 
    for (var i = s.length - 1; i >= 0; i--) {
        col += (s[i].charCodeAt(0) - 'A'.charCodeAt(0) + 1) * value;
        value *= 26;
    }
    return col;
};