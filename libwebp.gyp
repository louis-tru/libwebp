# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
	'variables': {
		'use_system_libwebp%': 0,
	},
	'conditions': [
		['use_system_libwebp==0', {
			'targets': [
				{
					'target_name': 'libwebp_dec',
					'type': 'static_library',
					'include_dirs': ['.'],
					'sources': [
						'src/dec/alpha.c',
						'src/dec/buffer.c',
						'src/dec/frame.c',
						'src/dec/idec.c',
						'src/dec/io.c',
						'src/dec/layer.c',
						'src/dec/quant.c',
						'src/dec/tree.c',
						'src/dec/vp8.c',
						'src/dec/vp8l.c',
						'src/dec/webp.c',
					],
				},
				{
					'target_name': 'libwebp_dsp',
					'type': 'static_library',
					'include_dirs': ['.'],
					'sources': [
						'src/dsp/cpu.c',
						'src/dsp/dec_neon.c',
						'src/dsp/dec_sse2.c',
						'src/dsp/dec.c',
						'src/dsp/enc_sse2.c',
						'src/dsp/enc.c',
						'src/dsp/lossless.c',
						'src/dsp/upsampling_sse2.c',
						'src/dsp/upsampling.c',
						'src/dsp/yuv.c',
					],
				},
				{
					'target_name': 'libwebp_enc',
					'type': 'static_library',
					'include_dirs': ['.'],
					'sources': [
						'src/enc/alpha.c',
						'src/enc/analysis.c',
						'src/enc/backward_references.c',
						'src/enc/config.c',
						'src/enc/cost.c',
						'src/enc/filter.c',
						'src/enc/frame.c',
						'src/enc/histogram.c',
						'src/enc/iterator.c',
						'src/enc/layer.c',
						'src/enc/picture.c',
						'src/enc/quant.c',
						'src/enc/syntax.c',
						'src/enc/tree.c',
						'src/enc/vp8l.c',
						'src/enc/webpenc.c',
					],
				},
				{
					'target_name': 'libwebp_mux',
					'type': 'static_library',
					'include_dirs': ['.'],
					'sources': [
						'src/mux/demux.c',
						'src/mux/muxedit.c',
						'src/mux/muxi.h',
						'src/mux/muxinternal.c',
						'src/mux/muxread.c',
					],
				},
				{
					'target_name': 'libwebp_utils',
					'type': 'static_library',
					'include_dirs': ['.'],
					'sources': [
						'src/utils/bit_reader.c',
						'src/utils/bit_writer.c',
						'src/utils/color_cache.c',
						'src/utils/filters.c',
						'src/utils/huffman_encode.c',
						'src/utils/huffman.c',
						'src/utils/quant_levels.c',
						'src/utils/rescaler.c',
						'src/utils/thread.c',
						'src/utils/utils.c',
					],
				},
				{
					'target_name': 'libwebp',
					'dependencies' : [
						'libwebp_dec',
						'libwebp_dsp',
						'libwebp_enc',
						'libwebp_mux',
						'libwebp_utils',
					],
					'direct_dependent_settings': {
						'include_dirs': ['./src'],
					},
					'conditions': [
						['library=="shared_library"', { 'type': '<(library)' }, { 'type': 'none' }],
						['OS!="win"', {'product_name': 'webp'}],
					],
				},
			],
		}, {
			'targets': [{
				'target_name': 'libwebp',
				'type': 'none',
				'direct_dependent_settings': {
					'defines': [
						'ENABLE_WEBP',
					],
				},
				'link_settings': {
					'libraries': [
						'-lwebp',
					],
				},
			}],
		}],
	],
}
