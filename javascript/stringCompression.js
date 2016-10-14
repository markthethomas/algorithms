import test from 'ava';

function stringCompression(str) {
  const chars = str.split('');
  let compressedString = '';
  let countConsecutive = 0;
  for (let i = 0; i < chars.length; i++) {
    countConsecutive += 1;
    if (i + 1 > chars.length || chars[i] !== chars[i + 1]) {
      compressedString += chars[i] + countConsecutive;
      countConsecutive = 0;
    }
  }
  // Don't compress if it's a bad idea! We could optimize by checking things beforehand somehow
  return compressedString.length < str.length ? compressedString : str;
}


test('stringCompression', (t) => {
  t.is(stringCompression('aabcccccaaa'), 'a2b1c5a3');
  t.is(stringCompression('mark'), 'mark');
  t.is(stringCompression('maaaaaark'), 'm1a6r1k1');
  t.is(stringCompression('blaaaaaaaaaaaaaaaaaargh'), 'b1l1a18r1g1h1');
});
