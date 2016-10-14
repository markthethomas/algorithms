import test from 'ava';

const question = [
    1,
    0,
    null,
    'Mark',
    'Mark',
    'b',
    { thing: false },
    { thing: false },
    true,
    false,
    false
];

const answer = [
  1,
  0,
  null,
  'Mark',
  'b',
  { thing: false },
  true,
  false,
];


function linearDedupe(arr) {
  return arr.filter((current, index, array) => array.indexOf(current) === index)
}

test('linearDedupe', t => {
  t.not(linearDedupe(question), answer, '');
});
