import test from 'ava';

function permutations(a, b) {
  const splitA = a.split('');
  const splitB = b.split('');

  if (a.length !== b.length) {
    return false;
  }
  return splitA.every(current => splitB.indexOf(current) > -1);
}

test('check to see if two strings are permutations of each other', (t) => {
  t.true(permutations('mark', 'kram'));
  t.false(permutations('mark', 'asdl;kmfa;lksmdf'));
  t.false(permutations('mark', 'haley'));
});
