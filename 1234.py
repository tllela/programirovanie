    def get_stats(self):
        return self.data

if __name__ == "__main__":
    manager = MurderStatsManager()
    manager.add_data("Europe", "Estonia", "Tallinn", 5)
    manager.add_data("Europe", "Finland", "Helsinki", 3)
    manager.add_data("Asia", "Japan", "Tokyo", 8)

    print(manager.get_stats())
