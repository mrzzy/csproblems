/*
 * CSProblems
 * 383. Ransom Note
*/

function countLetters(s: string): number[] {
  let letters: number[] = Array(26).fill(0);
  for (const c of s) {
    letters[c.charCodeAt(0) - "a".charCodeAt(0)] += 1;
  }

  return letters
}

export function canConstruct(ransomNote: string, magazine: string): boolean {
  // count letters we need to form the ransom note
  let needLetters = countLetters(ransomNote);
  // count letters we have in the magazine
  let haveLetters = countLetters(magazine);
  // check that we have the letters we need
  let nMissing = needLetters.reduce((nMissing, nNeed, letter) =>
    nMissing + Math.max(nNeed - haveLetters[letter], 0), 0);
  console.log(nMissing);
  return nMissing <= 0;
}
