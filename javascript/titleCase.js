import test from 'ava';

const questions = [
  'star wars',
  'the empire strikes back',
];

const answers = [
  'Star Wars',
  'The Empire Strikes Back',
];

function titleCaseWithLoop(str) {
  const words = str.split(' ');
  for (let i = 0; i < words.length; i++) {
    const currentWord = words[i];
    words[i] = currentWord.slice(0, 1).toUpperCase() + currentWord.slice(1);
  }
  return words.join(' ');
}

function titleCaseWithMap(str) {
  const words = str.split(' ');
  return words.map(word => word.slice(0, 1).toUpperCase() + word.slice(1)).join(' ');
}

test('titleCase (loop)', (t) => {
  questions.forEach((current, index) => {
    t.is(titleCaseWithLoop(current), answers[index]);
  });
});

test('titleCase (loop)', (t) => {
  questions.forEach((current, index) => {
    t.is(titleCaseWithMap(current), answers[index]);
  });
});
