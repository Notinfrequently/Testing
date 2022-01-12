class Worker:
    def __init__(self, level=7, per_rew=1, payment=70000):
        self._lvl = level
        self._pr = per_rew
        self._pay = payment
        self._bonus = 0.05
        self._mod = 1

    @property
    def level(self):
        return self._lvl

    @property
    def per_rew(self):
        return self._pr

    @property
    def payment(self):
        return self._pay

    @level.setter
    def level(self, lvl: int):
        """7 is a good start but you cant get higher then 17"""
        if not isinstance(lvl, int):
            raise ValueError
        if  lvl < 7 or lvl > 17:
            raise ValueError
        else:
            self._lvl = lvl
            if 7 < lvl < 10:
                self._bonus =  0.05
            elif 10 <= lvl < 13:
                self._bonus =  0.1
            elif 13 <= lvl < 15:
                self._bonus =  0.15
            elif lvl >= 15:
                self._bonus =  0.2

    @per_rew.setter
    def per_rew(self, pr: float):
        """Like in school from 1 to 5"""
        if not isinstance(pr, float):
            raise ValueError
        if  pr < 1.0 or pr > 5.0:
            raise ValueError
        else:
            self._pr = pr
            if pr < 2.0:
                self._mod = 1
            elif 2.0 <= pr < 2.5:
                self._mod =  1.25
            elif 2.5 <= pr < 3.0:
                self._mod =  1.5
            elif 3.0 <= pr < 3.5:
                self._mod =  2
            elif 3.5 <= pr < 4.0:
                self._mod =  2.5
            elif self._pr >= 4.0:
                self._mod =  3


    @payment.setter
    def payment(self, pay: int):
        """
        More then 70k but less then 750k
        """
        if not isinstance(pay, int):
            raise ValueError
        if  pay < 70000 or pay > 750000:
            raise ValueError
        else:
            self._pay = pay

    def bonus(self) -> int:
        return int(self._pay * self._bonus * self._mod)


if __name__ == "__main__":
    worker = Worker()
    # Wow, 0 payment job is the worst, can you change it for me please ?
    worker.payment = 100000
    worker.level = 10
    worker.per_rew = 2.5
    print(worker.bonus())