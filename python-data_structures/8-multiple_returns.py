#!/usr/bin/python3
if __name__ == "__main__":
    def multiple_returns(sentence):
        if len(sentence) == "":
            return len(sentence), sentence[0]
        else:
            return len(sentence), None
