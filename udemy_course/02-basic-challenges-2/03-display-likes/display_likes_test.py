import display_likes as dl


def test_display_likes():
    assert dl.display_likes([]) == 'no one likes this'
    assert dl.display_likes(['Peter']) == 'Peter likes this'
    assert dl.display_likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert dl.display_likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert dl.display_likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
    assert dl.display_likes(['Alex', 'Jacob', 'Mark', 'Max', 'Jill']) == 'Alex, Jacob and 3 others like this'
