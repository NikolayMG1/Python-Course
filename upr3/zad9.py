class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    @classmethod
    def from_str(cls, version_str):
        major, minor, patch = version_str.split('.')
        return cls(major, minor, patch)

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"

    def __eq__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)
        elif isinstance(other, str):
            other_version = Version.from_str(other)
            return self == other_version
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)
        elif isinstance(other, str):
            other_version = Version.from_str(other)
            return self < other_version
        return False

    def __gt__(self, other):
        if isinstance(other, Version):

            return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)
        elif isinstance(other, str):
            other_version = Version.from_str(other)
            return self > other_version
        return False

    def __hash__(self):
        return hash((self.major, self.minor, self.patch))



assert Version(1, 2, 3).major == 1
assert Version(1, 2, 3).minor == 2
assert Version(1, 2, 3).patch == 3
assert Version("1.2.3").major == 1
assert Version("1.2.3").minor == 2
assert Version("1.2.3").patch == 3
assert Version("10.2.304").major == 10
assert Version("10.2.304").minor == 2
assert Version("10.2.304").patch == 304
assert str(Version(1, 2, 3)) == "1.2.3"
assert repr(Version(1, 2, 3)) == "Version(1, 2, 3)"
assert Version(1, 2, 3) == Version(1, 2, 3)
assert Version(1, 2, 3) == "1.2.3"
assert Version(1, 2, 3) != Version(1, 2, 4)
assert Version(1, 2, 3) != "1.2.4"
assert Version(1, 2, 3) < Version(2, 0, 0)
assert Version(1, 2, 3) < "2.0.0"
assert Version(1, 2, 3) < Version(1, 3, 0)
assert Version(1, 2, 3) < "1.3.0"
assert Version(1, 2, 3) < Version(1, 2, 4)
assert Version(1, 2, 3) < "1.2.4"
assert Version("1.2.3") < Version("1.12.0")
assert Version("1.2.3") < "1.12.0"
assert Version(1, 2, 3) > Version(0, 9, 0)
assert Version(1, 2, 3) > "0.9.0"
assert Version(1, 2, 3) > Version(1, 1, 0)
assert Version(1, 2, 3) > "1.1.0"
assert Version(1, 2, 3) > Version(1, 2, 2)
assert Version(1, 2, 3) > "1.2.2"
assert Version("1.1.13") > Version("1.1.3")
assert Version("1.1.13") > "1.1.3"