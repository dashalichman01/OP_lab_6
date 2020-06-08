class Sending:
    def __init__(self, recipient, sender, insurance):
        self.recipient = recipient
        self.sender = sender
        self.insurance = insurance
    def resending(self):
        self.countresending += 1
        return self.countresending
    def poor_state(self):
        self.countpoor += 1
        if self.insurance == 'yes':
            print("Вы воспользовались страховкой")
        else:
            self.resending()
        return self.countpoor
    def success(self):
        self.countsuccess += 1
        print("Доставка была успешной")
class Letter(Sending):
    count = 0
    countresending = 0
    countpoor = 0
    countsuccess = 0
    def __init__(self, recipient, sender, insurance):
        Sending.__init__(self, recipient, sender, insurance)
        Letter.count += 1
    def rack_letter(self):
        d = {}
        d.setdefault('resipient', self.recipient)
        d.setdefault('sender', self.sender)
        d.setdefault('insurance', self.insurance)
        return d
    def resending(self):
        super().resending()
        Letter.countresending = self.countresending
    def poor_state(self):
        super().poor_state()
        Letter.countpoor = self.countpoor
    def success(self):
        super().success()
        Letter.countsuccess = self.countsuccess
class Package(Sending):
    count = 0
    countresending = 0
    countpoor = 0
    countsuccess = 0
    def __init__(self, recipient, sender, category, weight, size, type, insurance):
        Sending.__init__(self, recipient, sender, insurance)
        self.category = category
        self.type = type
        self.size = size
        self.weight = weight
        self.insurance = insurance
        Package.count += 1
    def rack_package(self):
        d = {}
        d.setdefault('resipient', self.recipient)
        d.setdefault('sender', self.sender)
        d.setdefault('category', self.category)
        d.setdefault('weight', self.weight)
        d.setdefault('size', self.size)
        d.setdefault('type', self.type)
        return d
    def resending(self):
        super().resending()
        Package.countresending = self.countresending
    def poor_state(self):
        super().poor_state()
        Package.countpoor = self.countpoor
    def success(self):
        super().success()
        Package.countsuccess = self.countsuccess
class Parcel(Sending):
    count = 0
    countresending = 0
    countpoor = 0
    countsuccess = 0
    def __init__(self, recipient, sender, category, weight, size, type, insurance):
        Sending.__init__(self, recipient, sender, insurance)
        self.category = category
        self.type = type
        self.size = size
        self.weight = weight
        Parcel.count += 1
    def rack_parcel(self):
        d = {}
        d.setdefault('resipient', self.recipient)
        d.setdefault('sender', self.sender)
        d.setdefault('category', self.category)
        d.setdefault('weight', self.weight)
        d.setdefault('size', self.size)
        d.setdefault('type', self.type)
        d.setdefault('insurance', self.insurance)
        return d
    def resending(self):
        super().resending()
        Parcel.countresending = self.countresending
    def poor_state(self):
        super().poor_state()
        Parcel.countpoor = self.countpoor
    def success(self):
        super().success()
        Parcel.countsuccess = self.countsuccess
print(("Всего зарегистрированных отправлений писем : {} ,Количество отправленных писем : {},Количество забракованных писем: {} , Количество возвращенных писем: {}").format(Letter.count, Letter.countsuccess, Letter.countpoor, Letter.countresending))
print(("Всего зарегистрированных отправлений посылок: {}, количество отправленных посылок : {}, количество забракованных посылок: {},количество возвращенных посылок: {}").format(Package.count, Package.countsuccess, Package.countpoor, Package.countresending))
print(("Всего зарегистрированных отправлений бандеролей: {}, количество отправленных бандеролей : {}, количество забракованных бандеролей: {},количество возвращенных бандеролей: {}").format(Parcel.count, Parcel.countsuccess, Parcel.countpoor, Parcel.countresending))
