import test from 'ava';

const questions = [
  'The quick brown fox jumped over the lazy dog',
  'May the force be with you',
  'Google do a barrel roll',
];

const answers = [
  6,
  5,
  6,
];

function findLongestWithLoop(str) {
  const words = str.split(' ');

  let longestWord = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > longestWord) {
      longestWord = words[i].length;
    }
  }
  return longestWord;
}

function findLongestWithStdLib(str) {
  const words = str.split(' ');
  const longestWord = words.sort((first, second) => second.length - first.length)[0];

  return longestWord.length;
}

function findeLongestWithReduce(str) {
  const words = str.split(' ');
  return words.reduce((longest, currentWord) => {
    if (currentWord.length > longest) {
      return currentWord.length
    } else {
      return longest;
    }
  }, 0)
}

test('find longest with std lib', t => {
  questions.forEach((current, index) =>  {
    t.is(findLongestWithStdLib(current), answers[index]);
  })
});

test('find longest with reduce', t => {
  questions.forEach((current, index) =>  {
    t.is(findeLongestWithReduce(current), answers[index]);
  })
});

test('find longest with loop', t => {
  questions.forEach((current, index) =>  {
    t.is(findLongestWithLoop(current), answers[index]);
  })
});
