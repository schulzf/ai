apt update
apt install p7zip-full p7zip-rar
git clone https://github.com/TheLastBen/diffusers
pip install -q git+https://github.com/TheLastBen/diffusers
pip install -q accelerate==0.12.0
pip install -q OmegaConf
pip install -q wget
pip install -q torchsde
pip install -q pytorch_lightning
pip install -q huggingface_hub
pip install -U -q --no-cache-dir gdown
wget https://github.com/TheLastBen/fast-stable-diffusion/raw/main/Dreambooth/Deps
mv Deps Deps.7z
7z x Deps.7z
cp -r /content/usr/local/lib/python3.7/dist-packages /usr/local/lib/python3.7/
rm Deps.7z
rm -r /content/usr
sed -i 's@else prefix + ": "@else prefix + ""@g' /usr/local/lib/python3.7/dist-packages/tqdm/std.py