def lengthOfLongestSubstring( s: str) -> int:
    maxStreak = 0
    currentCharacters = []
    streak = 0
    for character in s:
        if character in currentCharacters:
            streak -= currentCharacters.index(character)+1
            currentCharacters = currentCharacters[currentCharacters.index(character) + 1:]
        currentCharacters.append(character)
        streak += 1
        if maxStreak < streak:
            maxStreak = streak
    return maxStreak