import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivisella_tilavuudella_toimii(self):
        toinen_varasto = Varasto(-1)
        self.assertEqual(toinen_varasto.tilavuus, 0.0)

    def test_negatiivisella_alku_saldolla_toimii(self):
        kolmas_varasto = Varasto(0, -1)
        self.assertEqual(kolmas_varasto.saldo, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivisella_toimii(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_tilavuutta_suurempi_lisays_toimii(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liian_suuri_otto_palauttaa_ja_nollaa_saldon(self):
        saldo = self.varasto.saldo
        self.assertEqual(self.varasto.ota_varastosta(12), saldo)
        self.assertEqual(self.varasto.saldo, 0.0)
    
    def test_to_str(self):
        vastaus = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertEqual(self.varasto.__str__(), vastaus)