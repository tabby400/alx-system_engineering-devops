#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (let p = list.length - 1; p >= 0; p--) {
    revlist.push(list[p]); // iterates from last element
  }

  return revlist;
};
