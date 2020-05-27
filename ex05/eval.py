class Evaluator:

    @staticmethod
    def zip_evaluate(word, coef):
        if len(coef) != len(word):
            print(-1)
            return -1
        zpd = zip(word, coef)
        rep = 0
        for i in zpd:
            rep += len(i[0]) * i[1]
        print(rep)

    @staticmethod
    def enumerate_evaluate(word, coef):
        if len(coef) != len(word):
            print(-1)
            return -1
        enum = enumerate(word, 5)
        print(list(enum))
        pass

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coef = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(words, coef)
Evaluator.enumerate_evaluate(words, coef)