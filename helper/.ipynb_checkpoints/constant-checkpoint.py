PATH1 = './data/pregnant_women_ced.csv'
PATH2 = './data/pregnant_women.csv'
PATH3 = './data/toddlers_green.csv'
PATH4 = './data/toddlers_yellow.csv'
PATH5 = './data/toddlers_red.csv'

NEW_COLUMN_NAME = {'bps_nama_kabupaten_kota': 'regency',
                   'bps_nama_kecamatan': 'district',
                   'bps_nama_desa_kelurahan': 'sub_district',
                   'jumlah_ibu_hamil_mengalami_kek': 'pregnant_ced',
                  'jumlah_anak_pertumbuhan_hijau': 'toddler_green',
                  'jumlah_anak_pertumbuhan_kuning': 'toddler_yellow',
                  'jumlah_anak_pertumbuhan_merah': 'toddler_red',
                  'tahun': 'year',
                  'jumlah_ibu_hamil': 'pregnant_all'}