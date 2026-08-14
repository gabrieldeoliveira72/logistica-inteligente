"""
Testes unitários para o módulo de detecção de fadiga.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.fatigue_detector import FatigueDetector


class TestFatigueDetector(unittest.TestCase):

    def setUp(self):
        self.detector = FatigueDetector()

    def test_low_fatigue(self):
        driver_data = {
            'driving_hours': 1,
            'blink_rate': 0.2,
            'steering_adjustments': 0.2,
            'current_time': '10:00'
        }
        result = self.detector.detect_fatigue(driver_data)
        self.assertEqual(result['fatigue_level'], 'baixo')
        self.assertFalse(result['needs_rest'])
        self.assertFalse(result['critical'])

    def test_critical_fatigue(self):
        driver_data = {
            'driving_hours': 10,
            'blink_rate': 0.9,
            'steering_adjustments': 0.9,
            'current_time': '03:00'  # madrugada aumenta fator
        }
        result = self.detector.detect_fatigue(driver_data)
        self.assertTrue(result['needs_rest'])
        self.assertIn(result['fatigue_level'], ['alto', 'crítico'])


if __name__ == '__main__':
    unittest.main()
