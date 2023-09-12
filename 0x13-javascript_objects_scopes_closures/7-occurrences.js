#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let p = 0; p < list.length; p++) {
    if (list[p] === searchElement) {
      total++;
    }
  }

  return total;
};
