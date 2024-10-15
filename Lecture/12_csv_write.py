# Python: CSV write
import.csv
cars = [
    ('Make', {'TOYOTA', 'Ford'}),
    ('Model', {'RAV4', 'F150'}),
    ('Max Speed', {220, 190}),
    ('Power', {195, 320})
]

for r in cars:
    print(r)

with open("cars.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow([r(0) for r in cars])
    