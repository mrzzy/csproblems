/*
 * CSProblems
 * 383. Ransom Note
 * Unit Tests
*/

import { canConstruct } from "./index";

describe("countLetters()", () => {
  it("accepts ransomNote that can be formed with magazine", () => expect(canConstruct("aa", "aab")).toBeTruthy()
  );
  it("rejects ransomNote that cannot be formed with magazine", () => expect(canConstruct("abbc", "abcd")).toBeFalsy()
  );
});
