import test from 'ava';

const questions = [
  'ava',
  'racecar',
  'race car',
  'aaa bb b a aa',
  'neven',
  'Mark',
  '0_0 (: /-\ :) 0–0',
];

const answers = [
  true,
  true,
  true,
  true,
  true,
  false,
  true
];

function isPalindrome(str) {
  if (typeof str !== 'string') {
    return false;
  }
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, '');
  return normalizedStr.split('').reverse().join('') === normalizedStr;
}

function isPalindromeManual(str) {
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, '');
  const len = str.length;
  for (let i = 0; i < len/2; i++) {
    console.log(normalizedStr[i], normalizedStr[len - 1 - i]);
    if (normalizedStr[i] !== str[len - 1 - i]) {
      return false;
    }
  }
  return true;
}


test('palindrome w/ std lib', t => {
  questions.forEach((current, index) =>  {
    t.is(isPalindrome(current), answers[index]);
  })
});

test('palindrome w/ std lib', t => {
  questions.forEach((current, index) =>  {
    t.is(isPalindromeManual(current), answers[index]);
  })
});
