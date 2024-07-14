import argparse
from quant_matrix import QuantizationMatrix
from helper_utils1 import (
    read_img, create_quantize_dct, lexographic_sort, shift_vector_thresh, display_results
)

if __name__ == "__main__":

    # Create the parser


    img_path = "images/forged1.png"
    block_size = 500
    qf = 500
    shift_thresh = 500
    stride = 500
    # 8x8 quantization matrix based on QF
    Q_8x8 = QuantizationMatrix().get_qm(qf)

    # read img
    img, original_image, overlay, width, height = read_img(img_path)

    # DCT
    quant_row_matrices = create_quantize_dct(img, width, height, block_size, stride, Q_8x8)

    # lexographic sort
    shift_vec_count, matched_blocks = lexographic_sort(quant_row_matrices)

    # shift vector threhsolding
    matched_pixels_start = shift_vector_thresh(shift_vec_count, matched_blocks, shift_thresh)

    # displaying output
    display_results(overlay, original_image, matched_pixels_start, block_size)