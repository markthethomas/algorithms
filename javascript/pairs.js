function unbalancedSummationPairs(arr, sum) {
  const sum = sum;
	return arr.map(item => {
    arr.map(nextItem => {
    	if ((item + nextItem === sum) && (nextItem !== item)) {
      	return [item, nextItem];
      }
    });
  });
}
