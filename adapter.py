class Old:
    def get(self):
        return "12345"


class New:
    def get(self):
        return 54321


class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())


def main(obj):
    print(f"Результат работы вернул: " + obj.get())


if __name__ == "__main__":
    o = Old()
    main(o)

    o2 = New()
    try:
        main(o2)
    except TypeError as e:
        print(e)

    o3 = Adapter()
    main(o3)
