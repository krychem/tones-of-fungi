# tones-of-fungi

Turning the electrical signals of fungi (and other living things) into sound. Python + ESP32.

## Status

Work in progress. Currently: simulating

## Quick start

```bash
git clone https://github.com/krychem/tones-of-fungi
cd tones-of-fungi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python steps/step01_noise.py
```

## Project structure

- `steps/` - learning scripts, one small step each
- `core/` - pure Python logic (filters, detection), runs on PC and ESP32
- `sources/`, `outputs/` - where the signal comes from and where it goes
- `docs/devlog.md` - development notes

## Roadmap

- [ ] v0.1 - signal simulation and processing (PC)
- [ ] v0.2 - real signal from EXP32, sound output
- [ ] v0.3 - physical mallets

## License

MIT