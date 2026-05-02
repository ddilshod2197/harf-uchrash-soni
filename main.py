def daraja_tanlash(yosh):
    if 21 <= yosh <= 45:
        return "O'rta daraja"
    else:
        return "Boshqa daraja"

yosh = int(input("Yoshingiz nechida? "))
print(daraja_tanlash(yosh))
```

```python
def daraja_tanlash(yosh):
    daraja = "O'rta daraja" if 21 <= yosh <= 45 else "Boshqa daraja"
    return daraja

yosh = int(input("Yoshingiz nechida? "))
print(daraja_tanlash(yosh))
