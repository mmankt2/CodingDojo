//zip arrays into map
function zipArrMap(arr1, arr2){
  var len = arr1.length;
  var arrMap = {};
  for (var i = 0; i < len; i++){
    arrMap[arr1[i]] = arr2[i];
  }
  return arrMap;
}
console.log(zipArrMap(["abc", 3, "yo"],[42, "wassup", true]))

//invert hash
function invertHash(assocArr){
  var new_object = {};
  for (key in assocArr){
    new_object[assocArr[key]] = key;
  }
  return new_object;
}
console.log(invertHash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))

//number of values without length
function numVals(obj){
  var count = 0;
  for (key in obj){
    if (obj[key]){
      count++;
    }
  }
  return count;
}
console.log(numVals({band: "Travis Shredd & the Good Ol’ Homeboys", style: "Country/Metal/Rap", album: "668: The Neighbor of the Beast"}))