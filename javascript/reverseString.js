import test from 'ava';

const questions = [
    'Mark',
    'a a a a a a a',
    'blammo',
    'copa vidA'
]

const answers = [
    'kraM',
    'a a a a a a a',
    'ommalb',
    'Adiv apoc'
]

const input = 'library';

// "Std" lib
function stdLibReverse(str) {
    return str.split('').reverse().join('');
}

// Recursive
function recursiveReverse(str) {
    if (str === "") {
        return "";
    } else {
        return recursiveReverse(str.slice(1)) + str.slice(0,1);
    }
}

function manualLoopReverse(str) {
    let newString = '';
    for (let i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}

test('manual with loop', t => {
    questions.forEach((question, index) => {
        t.is(recursiveReverse(question), answers[index]);
    })
});

test('manual with loop', t => {
    questions.forEach((question, index) => {
        t.is(manualLoopReverse(question), answers[index]);
    })
});

test('std lib approach', t => {
    questions.forEach((question, index) => {
        t.is(stdLibReverse(question), answers[index]);
    })
});
