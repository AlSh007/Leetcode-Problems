return count
    

    def isPrime(self, setBits):
        if setBits <= 1:
            return False
        

        for i in range(2, int(setBits ** 0.5) + 1):
            if setBits % i == 0:
                return False

        return True