#!/usr/bin/env python
import sys
from argparse import ArgumentParser
from os.path import splitext, basename, dirname, join
from typing import List, Tuple

from PIL import Image


def resize_over(img: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
    # サイズオーバーを許容したリサイズ
    w, h = img.size
    tw, th = target_size
    # 拡大・縮小率
    rw, rh = tw / w, th / h
    mr = max(rw, rh)  # 大きい方を取る
    return img.resize((int(mr * w), int(mr * h)), Image.BICUBIC)


def trim_center(img: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
    # 中央を基準にして指定サイズでトリム
    w, h = img.size
    tw, th = target_size
    cx, cy = abs(tw - w) / 2, abs(th - h) / 2
    crop_size = (int(cx), int(cy), int(cx + tw), int(cy + th))
    return img.crop(crop_size)


def main(argv: List[str]):
    parser = ArgumentParser()
    parser.add_argument('image_path')
    parser.add_argument('-W', '--width', dest='width', default=1920, type=int)
    parser.add_argument('-H', '--height', dest='height', default=1080, type=int)
    opt = parser.parse_args(argv)

    image_path = opt.image_path
    tw, th = opt.width, opt.height
    target_size = tw, th

    src_img = Image.open(image_path)

    # リサイズ
    resized_img = resize_over(src_img, target_size)

    # トリミング
    trimmed_img = trim_center(resized_img, target_size)

    # 保存
    dir_path = dirname(image_path)
    name, ext = (splitext(basename(image_path)) + ('.png',))[:2]
    new_name = '{}-trim{}'.format(name, ext)
    trimmed_img.save(join(dir_path, new_name))


if __name__ == '__main__':
    main(sys.argv[1:])
