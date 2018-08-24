# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the 'tests' package
from unittest import TestCase
from console_progressbar import ProgressBar


class TestConsoleProgressBar(TestCase):
    def setUp(self):
        self.total = 100

    def test_can_create_an_instance(self):
        pb = ProgressBar(self.total)
        self.assertIsInstance(pb,ProgressBar)
    
    def test_it_has_custom_prefix(self):
        pb = ProgressBar(self.total, prefix='Test')
        self.assertTrue('Test' in pb.generate_pbar(50))
        
    
    def test_it_has_custom_suffix(self):
        pb = ProgressBar(self.total, suffix='Test')
        self.assertTrue('Test' in pb.generate_pbar(50))
    
    def test_it_has_custom_fill(self):
        pb = ProgressBar(self.total, fill='X')
        self.assertTrue('X' in pb.generate_pbar(50))
    
    def test_it_has_custom_zero_fill(self):
        pb = ProgressBar(self.total, zfill='=')
        self.assertTrue('=' in pb.generate_pbar(50))
        self.assertEqual(50, pb.generate_pbar(50).count('='))
    
    def test_it_has_custom_bar_length(self):
        pb = ProgressBar(self.total, length = 10)
        # at 0% should be only 10 '-'
        self.assertEqual(10, pb.generate_pbar(0).count('-'))
        # at 10% should be only 9 '-'
        self.assertEqual(9, pb.generate_pbar(10).count('-'))
        # at 50% should be only 5 '-'
        self.assertEqual(5, pb.generate_pbar(50).count('-'))
        # at 90% should be only 1 '-'
        self.assertEqual(1, pb.generate_pbar(90).count('-'))
        # at 100% should be only 0 '-'
        self.assertEqual(0, pb.generate_pbar(100).count('-'))
    
    def test_it_has_custom_decimals_places(self):
        pb = ProgressBar(98, decimals = 1)
        # 100*42/98 = 42,85714285714285714286
        self.assertRegexpMatches(pb.generate_pbar(42),r'\.\d{1}\%')
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{2}\%')
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{3}\%')
        pb = ProgressBar(98, decimals = 2)
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{1}\%')
        self.assertRegexpMatches(pb.generate_pbar(42),r'\.\d{2}\%')
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{3}\%')
        pb = ProgressBar(98, decimals = 3)
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{1}\%')
        self.assertNotRegexpMatches(pb.generate_pbar(42),r'\.\d{2}\%')
        self.assertRegexpMatches(pb.generate_pbar(42),r'\.\d{3}\%')

