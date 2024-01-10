module LibJpeg

using JpegTurbo_jll
export JpegTurbo_jll

using CEnum

const LIBJPEG_TURBO_VERSION = v"3.0.1"

const boolean = @static Sys.iswindows() ? Cuchar : Cint



struct __JL_Ctag_12
    data::NTuple{80, UInt8}
end

function Base.getproperty(x::Ptr{__JL_Ctag_12}, f::Symbol)
    f === :i && return Ptr{NTuple{8, Cint}}(x + 0)
    f === :s && return Ptr{NTuple{80, Cchar}}(x + 0)
    return getfield(x, f)
end

function Base.getproperty(x::__JL_Ctag_12, f::Symbol)
    r = Ref{__JL_Ctag_12}(x)
    ptr = Base.unsafe_convert(Ptr{__JL_Ctag_12}, r)
    fptr = getproperty(ptr, f)
    GC.@preserve r unsafe_load(fptr)
end

function Base.setproperty!(x::Ptr{__JL_Ctag_12}, f::Symbol, v)
    unsafe_store!(getproperty(x, f), v)
end

struct jpeg_error_mgr
    data::NTuple{168, UInt8}
end

function Base.getproperty(x::Ptr{jpeg_error_mgr}, f::Symbol)
    f === :error_exit && return Ptr{Ptr{Cvoid}}(x + 0)
    f === :emit_message && return Ptr{Ptr{Cvoid}}(x + 8)
    f === :output_message && return Ptr{Ptr{Cvoid}}(x + 16)
    f === :format_message && return Ptr{Ptr{Cvoid}}(x + 24)
    f === :reset_error_mgr && return Ptr{Ptr{Cvoid}}(x + 32)
    f === :msg_code && return Ptr{Cint}(x + 40)
    f === :msg_parm && return Ptr{__JL_Ctag_12}(x + 44)
    f === :trace_level && return Ptr{Cint}(x + 124)
    f === :num_warnings && return Ptr{Clong}(x + 128)
    f === :jpeg_message_table && return Ptr{Ptr{Ptr{Cchar}}}(x + 136)
    f === :last_jpeg_message && return Ptr{Cint}(x + 144)
    f === :addon_message_table && return Ptr{Ptr{Ptr{Cchar}}}(x + 152)
    f === :first_addon_message && return Ptr{Cint}(x + 160)
    f === :last_addon_message && return Ptr{Cint}(x + 164)
    return getfield(x, f)
end

function Base.getproperty(x::jpeg_error_mgr, f::Symbol)
    r = Ref{jpeg_error_mgr}(x)
    ptr = Base.unsafe_convert(Ptr{jpeg_error_mgr}, r)
    fptr = getproperty(ptr, f)
    GC.@preserve r unsafe_load(fptr)
end

function Base.setproperty!(x::Ptr{jpeg_error_mgr}, f::Symbol, v)
    unsafe_store!(getproperty(x, f), v)
end

struct jpeg_memory_mgr
    alloc_small::Ptr{Cvoid}
    alloc_large::Ptr{Cvoid}
    alloc_sarray::Ptr{Cvoid}
    alloc_barray::Ptr{Cvoid}
    request_virt_sarray::Ptr{Cvoid}
    request_virt_barray::Ptr{Cvoid}
    realize_virt_arrays::Ptr{Cvoid}
    access_virt_sarray::Ptr{Cvoid}
    access_virt_barray::Ptr{Cvoid}
    free_pool::Ptr{Cvoid}
    self_destruct::Ptr{Cvoid}
    max_memory_to_use::Clong
    max_alloc_chunk::Clong
end

struct jpeg_progress_mgr
    progress_monitor::Ptr{Cvoid}
    pass_counter::Clong
    pass_limit::Clong
    completed_passes::Cint
    total_passes::Cint
end

const JOCTET = Cuchar

struct jpeg_destination_mgr
    next_output_byte::Ptr{JOCTET}
    free_in_buffer::Csize_t
    init_destination::Ptr{Cvoid}
    empty_output_buffer::Ptr{Cvoid}
    term_destination::Ptr{Cvoid}
end

const JDIMENSION = Cuint

@cenum J_COLOR_SPACE::UInt32 begin
    JCS_UNKNOWN = 0
    JCS_GRAYSCALE = 1
    JCS_RGB = 2
    JCS_YCbCr = 3
    JCS_CMYK = 4
    JCS_YCCK = 5
    JCS_EXT_RGB = 6
    JCS_EXT_RGBX = 7
    JCS_EXT_BGR = 8
    JCS_EXT_BGRX = 9
    JCS_EXT_XBGR = 10
    JCS_EXT_XRGB = 11
    JCS_EXT_RGBA = 12
    JCS_EXT_BGRA = 13
    JCS_EXT_ABGR = 14
    JCS_EXT_ARGB = 15
    JCS_RGB565 = 16
end

const UINT16 = Cushort

mutable struct JQUANT_TBL
    quantval::NTuple{64, UINT16}
    sent_table::boolean
    JQUANT_TBL() = new()
end

mutable struct jpeg_component_info
    component_id::Cint
    component_index::Cint
    h_samp_factor::Cint
    v_samp_factor::Cint
    quant_tbl_no::Cint
    dc_tbl_no::Cint
    ac_tbl_no::Cint
    width_in_blocks::JDIMENSION
    height_in_blocks::JDIMENSION
    DCT_h_scaled_size::Cint
    DCT_v_scaled_size::Cint
    downsampled_width::JDIMENSION
    downsampled_height::JDIMENSION
    component_needed::boolean
    MCU_width::Cint
    MCU_height::Cint
    MCU_blocks::Cint
    MCU_sample_width::Cint
    last_col_width::Cint
    last_row_height::Cint
    quant_table::Ptr{JQUANT_TBL}
    dct_table::Ptr{Cvoid}
    jpeg_component_info() = new()
end

const UINT8 = Cuchar

mutable struct JHUFF_TBL
    bits::NTuple{17, UINT8}
    huffval::NTuple{256, UINT8}
    sent_table::boolean
    JHUFF_TBL() = new()
end

mutable struct jpeg_scan_info
    comps_in_scan::Cint
    component_index::NTuple{4, Cint}
    Ss::Cint
    Se::Cint
    Ah::Cint
    Al::Cint
    jpeg_scan_info() = new()
end

@cenum J_DCT_METHOD::UInt32 begin
    JDCT_ISLOW = 0
    JDCT_IFAST = 1
    JDCT_FLOAT = 2
end

const jpeg_comp_master = Cvoid

const jpeg_c_main_controller = Cvoid

const jpeg_c_prep_controller = Cvoid

const jpeg_c_coef_controller = Cvoid

const jpeg_marker_writer = Cvoid

const jpeg_color_converter = Cvoid

const jpeg_downsampler = Cvoid

const jpeg_forward_dct = Cvoid

const jpeg_entropy_encoder = Cvoid

mutable struct jpeg_compress_struct
    err::Ptr{jpeg_error_mgr}
    mem::Ptr{jpeg_memory_mgr}
    progress::Ptr{jpeg_progress_mgr}
    client_data::Ptr{Cvoid}
    is_decompressor::boolean
    global_state::Cint
    dest::Ptr{jpeg_destination_mgr}
    image_width::JDIMENSION
    image_height::JDIMENSION
    input_components::Cint
    in_color_space::J_COLOR_SPACE
    input_gamma::Cdouble
    scale_num::Cuint
    scale_denom::Cuint
    jpeg_width::JDIMENSION
    jpeg_height::JDIMENSION
    data_precision::Cint
    num_components::Cint
    jpeg_color_space::J_COLOR_SPACE
    comp_info::Ptr{jpeg_component_info}
    quant_tbl_ptrs::NTuple{4, Ptr{JQUANT_TBL}}
    q_scale_factor::NTuple{4, Cint}
    dc_huff_tbl_ptrs::NTuple{4, Ptr{JHUFF_TBL}}
    ac_huff_tbl_ptrs::NTuple{4, Ptr{JHUFF_TBL}}
    arith_dc_L::NTuple{16, UINT8}
    arith_dc_U::NTuple{16, UINT8}
    arith_ac_K::NTuple{16, UINT8}
    num_scans::Cint
    scan_info::Ptr{jpeg_scan_info}
    raw_data_in::boolean
    arith_code::boolean
    optimize_coding::boolean
    CCIR601_sampling::boolean
    do_fancy_downsampling::boolean
    smoothing_factor::Cint
    dct_method::J_DCT_METHOD
    restart_interval::Cuint
    restart_in_rows::Cint
    write_JFIF_header::boolean
    JFIF_major_version::UINT8
    JFIF_minor_version::UINT8
    density_unit::UINT8
    X_density::UINT16
    Y_density::UINT16
    write_Adobe_marker::boolean
    next_scanline::JDIMENSION
    progressive_mode::boolean
    max_h_samp_factor::Cint
    max_v_samp_factor::Cint
    min_DCT_h_scaled_size::Cint
    min_DCT_v_scaled_size::Cint
    total_iMCU_rows::JDIMENSION
    comps_in_scan::Cint
    cur_comp_info::NTuple{4, Ptr{jpeg_component_info}}
    MCUs_per_row::JDIMENSION
    MCU_rows_in_scan::JDIMENSION
    blocks_in_MCU::Cint
    MCU_membership::NTuple{10, Cint}
    Ss::Cint
    Se::Cint
    Ah::Cint
    Al::Cint
    block_size::Cint
    natural_order::Ptr{Cint}
    lim_Se::Cint
    master::Ptr{jpeg_comp_master}
    main::Ptr{jpeg_c_main_controller}
    prep::Ptr{jpeg_c_prep_controller}
    coef::Ptr{jpeg_c_coef_controller}
    marker::Ptr{jpeg_marker_writer}
    cconvert::Ptr{jpeg_color_converter}
    downsample::Ptr{jpeg_downsampler}
    fdct::Ptr{jpeg_forward_dct}
    entropy::Ptr{jpeg_entropy_encoder}
    script_space::Ptr{jpeg_scan_info}
    script_space_size::Cint
    jpeg_compress_struct() = new()
end
function Base.getproperty(x::Ptr{jpeg_compress_struct}, f::Symbol)
    f === :err && return Ptr{Ptr{jpeg_error_mgr}}(x + 0)
    f === :mem && return Ptr{Ptr{jpeg_memory_mgr}}(x + 8)
    f === :progress && return Ptr{Ptr{jpeg_progress_mgr}}(x + 16)
    f === :client_data && return Ptr{Ptr{Cvoid}}(x + 24)
    f === :is_decompressor && return Ptr{boolean}(x + 32)
    f === :global_state && return Ptr{Cint}(x + 36)
    f === :dest && return Ptr{Ptr{jpeg_destination_mgr}}(x + 40)
    f === :image_width && return Ptr{JDIMENSION}(x + 48)
    f === :image_height && return Ptr{JDIMENSION}(x + 52)
    f === :input_components && return Ptr{Cint}(x + 56)
    f === :in_color_space && return Ptr{J_COLOR_SPACE}(x + 60)
    f === :input_gamma && return Ptr{Cdouble}(x + 64)
    f === :scale_num && return Ptr{Cuint}(x + 72)
    f === :scale_denom && return Ptr{Cuint}(x + 76)
    f === :jpeg_width && return Ptr{JDIMENSION}(x + 80)
    f === :jpeg_height && return Ptr{JDIMENSION}(x + 84)
    f === :data_precision && return Ptr{Cint}(x + 88)
    f === :num_components && return Ptr{Cint}(x + 92)
    f === :jpeg_color_space && return Ptr{J_COLOR_SPACE}(x + 96)
    f === :comp_info && return Ptr{Ptr{jpeg_component_info}}(x + 104)
    f === :quant_tbl_ptrs && return Ptr{NTuple{4, Ptr{JQUANT_TBL}}}(x + 112)
    f === :q_scale_factor && return Ptr{NTuple{4, Cint}}(x + 144)
    f === :dc_huff_tbl_ptrs && return Ptr{NTuple{4, Ptr{JHUFF_TBL}}}(x + 160)
    f === :ac_huff_tbl_ptrs && return Ptr{NTuple{4, Ptr{JHUFF_TBL}}}(x + 192)
    f === :arith_dc_L && return Ptr{NTuple{16, UINT8}}(x + 224)
    f === :arith_dc_U && return Ptr{NTuple{16, UINT8}}(x + 240)
    f === :arith_ac_K && return Ptr{NTuple{16, UINT8}}(x + 256)
    f === :num_scans && return Ptr{Cint}(x + 272)
    f === :scan_info && return Ptr{Ptr{jpeg_scan_info}}(x + 280)
    f === :raw_data_in && return Ptr{boolean}(x + 288)
    f === :arith_code && return Ptr{boolean}(x + 292)
    f === :optimize_coding && return Ptr{boolean}(x + 296)
    f === :CCIR601_sampling && return Ptr{boolean}(x + 300)
    f === :do_fancy_downsampling && return Ptr{boolean}(x + 304)
    f === :smoothing_factor && return Ptr{Cint}(x + 308)
    f === :dct_method && return Ptr{J_DCT_METHOD}(x + 312)
    f === :restart_interval && return Ptr{Cuint}(x + 316)
    f === :restart_in_rows && return Ptr{Cint}(x + 320)
    f === :write_JFIF_header && return Ptr{boolean}(x + 324)
    f === :JFIF_major_version && return Ptr{UINT8}(x + 328)
    f === :JFIF_minor_version && return Ptr{UINT8}(x + 329)
    f === :density_unit && return Ptr{UINT8}(x + 330)
    f === :X_density && return Ptr{UINT16}(x + 332)
    f === :Y_density && return Ptr{UINT16}(x + 334)
    f === :write_Adobe_marker && return Ptr{boolean}(x + 336)
    f === :next_scanline && return Ptr{JDIMENSION}(x + 340)
    f === :progressive_mode && return Ptr{boolean}(x + 344)
    f === :max_h_samp_factor && return Ptr{Cint}(x + 348)
    f === :max_v_samp_factor && return Ptr{Cint}(x + 352)
    f === :min_DCT_h_scaled_size && return Ptr{Cint}(x + 356)
    f === :min_DCT_v_scaled_size && return Ptr{Cint}(x + 360)
    f === :total_iMCU_rows && return Ptr{JDIMENSION}(x + 364)
    f === :comps_in_scan && return Ptr{Cint}(x + 368)
    f === :cur_comp_info && return Ptr{NTuple{4, Ptr{jpeg_component_info}}}(x + 376)
    f === :MCUs_per_row && return Ptr{JDIMENSION}(x + 408)
    f === :MCU_rows_in_scan && return Ptr{JDIMENSION}(x + 412)
    f === :blocks_in_MCU && return Ptr{Cint}(x + 416)
    f === :MCU_membership && return Ptr{NTuple{10, Cint}}(x + 420)
    f === :Ss && return Ptr{Cint}(x + 460)
    f === :Se && return Ptr{Cint}(x + 464)
    f === :Ah && return Ptr{Cint}(x + 468)
    f === :Al && return Ptr{Cint}(x + 472)
    f === :block_size && return Ptr{Cint}(x + 476)
    f === :natural_order && return Ptr{Ptr{Cint}}(x + 480)
    f === :lim_Se && return Ptr{Cint}(x + 488)
    f === :master && return Ptr{Ptr{jpeg_comp_master}}(x + 496)
    f === :main && return Ptr{Ptr{jpeg_c_main_controller}}(x + 504)
    f === :prep && return Ptr{Ptr{jpeg_c_prep_controller}}(x + 512)
    f === :coef && return Ptr{Ptr{jpeg_c_coef_controller}}(x + 520)
    f === :marker && return Ptr{Ptr{jpeg_marker_writer}}(x + 528)
    f === :cconvert && return Ptr{Ptr{jpeg_color_converter}}(x + 536)
    f === :downsample && return Ptr{Ptr{jpeg_downsampler}}(x + 544)
    f === :fdct && return Ptr{Ptr{jpeg_forward_dct}}(x + 552)
    f === :entropy && return Ptr{Ptr{jpeg_entropy_encoder}}(x + 560)
    f === :script_space && return Ptr{Ptr{jpeg_scan_info}}(x + 568)
    f === :script_space_size && return Ptr{Cint}(x + 576)
    return getfield(x, f)
end

function Base.setproperty!(x::Ptr{jpeg_compress_struct}, f::Symbol, v)
    unsafe_store!(getproperty(x, f), v)
end


const j_compress_ptr = Ptr{jpeg_compress_struct}

function jpeg_CreateCompress(cinfo, version, structsize)
    ccall((:jpeg_CreateCompress, libjpeg), Cvoid, (j_compress_ptr, Cint, Csize_t), cinfo, version, structsize)
end

mutable struct __JL_jpeg_decompress_struct
end

function Base.unsafe_load(x::Ptr{__JL_jpeg_decompress_struct})
    unsafe_load(Ptr{jpeg_decompress_struct}(x))
end

function Base.getproperty(x::Ptr{__JL_jpeg_decompress_struct}, f::Symbol)
    getproperty(Ptr{jpeg_decompress_struct}(x), f)
end

function Base.setproperty!(x::Ptr{__JL_jpeg_decompress_struct}, f::Symbol, v)
    setproperty!(Ptr{jpeg_decompress_struct}(x), f, v)
end

Base.unsafe_convert(::Type{Ptr{__JL_jpeg_decompress_struct}}, x::Ref) = Base.unsafe_convert(Ptr{__JL_jpeg_decompress_struct}, Base.unsafe_convert(Ptr{jpeg_decompress_struct}, x))

Base.unsafe_convert(::Type{Ptr{__JL_jpeg_decompress_struct}}, x::Ptr) = Ptr{__JL_jpeg_decompress_struct}(x)

const j_decompress_ptr = Ptr{__JL_jpeg_decompress_struct}

function jpeg_CreateDecompress(cinfo, version, structsize)
    ccall((:jpeg_CreateDecompress, libjpeg), Cvoid, (j_decompress_ptr, Cint, Csize_t), cinfo, version, structsize)
end

const JSAMPLE = Cuchar

const J12SAMPLE = Cshort

const J16SAMPLE = Cushort

const JCOEF = Cshort

const INT16 = Cshort

const INT32 = Clong

const JSAMPROW = Ptr{JSAMPLE}

const JSAMPARRAY = Ptr{JSAMPROW}

const JSAMPIMAGE = Ptr{JSAMPARRAY}

const J12SAMPROW = Ptr{J12SAMPLE}

const J12SAMPARRAY = Ptr{J12SAMPROW}

const J12SAMPIMAGE = Ptr{J12SAMPARRAY}

const J16SAMPROW = Ptr{J16SAMPLE}

const J16SAMPARRAY = Ptr{J16SAMPROW}

const J16SAMPIMAGE = Ptr{J16SAMPARRAY}

const JBLOCK = NTuple{64, JCOEF}

const JBLOCKROW = Ptr{JBLOCK}

const JBLOCKARRAY = Ptr{JBLOCKROW}

const JBLOCKIMAGE = Ptr{JBLOCKARRAY}

const JCOEFPTR = Ptr{JCOEF}

mutable struct __JL_jpeg_marker_struct
end

function Base.unsafe_load(x::Ptr{__JL_jpeg_marker_struct})
    unsafe_load(Ptr{jpeg_marker_struct}(x))
end

function Base.getproperty(x::Ptr{__JL_jpeg_marker_struct}, f::Symbol)
    getproperty(Ptr{jpeg_marker_struct}(x), f)
end

function Base.setproperty!(x::Ptr{__JL_jpeg_marker_struct}, f::Symbol, v)
    setproperty!(Ptr{jpeg_marker_struct}(x), f, v)
end

Base.unsafe_convert(::Type{Ptr{__JL_jpeg_marker_struct}}, x::Ref) = Base.unsafe_convert(Ptr{__JL_jpeg_marker_struct}, Base.unsafe_convert(Ptr{jpeg_marker_struct}, x))

Base.unsafe_convert(::Type{Ptr{__JL_jpeg_marker_struct}}, x::Ptr) = Ptr{__JL_jpeg_marker_struct}(x)

const jpeg_saved_marker_ptr = Ptr{__JL_jpeg_marker_struct}

mutable struct jpeg_marker_struct
    next::jpeg_saved_marker_ptr
    marker::UINT8
    original_length::Cuint
    data_length::Cuint
    data::Ptr{JOCTET}
    jpeg_marker_struct() = new()
end

@cenum J_DITHER_MODE::UInt32 begin
    JDITHER_NONE = 0
    JDITHER_ORDERED = 1
    JDITHER_FS = 2
end

mutable struct jpeg_common_struct
    err::Ptr{jpeg_error_mgr}
    mem::Ptr{jpeg_memory_mgr}
    progress::Ptr{jpeg_progress_mgr}
    client_data::Ptr{Cvoid}
    is_decompressor::boolean
    global_state::Cint
    jpeg_common_struct() = new()
end

const j_common_ptr = Ptr{jpeg_common_struct}

struct jpeg_source_mgr
    next_input_byte::Ptr{JOCTET}
    bytes_in_buffer::Csize_t
    init_source::Ptr{Cvoid}
    fill_input_buffer::Ptr{Cvoid}
    skip_input_data::Ptr{Cvoid}
    resync_to_restart::Ptr{Cvoid}
    term_source::Ptr{Cvoid}
end

const jpeg_decomp_master = Cvoid

const jpeg_d_main_controller = Cvoid

const jpeg_d_coef_controller = Cvoid

const jpeg_d_post_controller = Cvoid

const jpeg_input_controller = Cvoid

const jpeg_marker_reader = Cvoid

const jpeg_entropy_decoder = Cvoid

const jpeg_inverse_dct = Cvoid

const jpeg_upsampler = Cvoid

const jpeg_color_deconverter = Cvoid

const jpeg_color_quantizer = Cvoid

mutable struct jpeg_decompress_struct
    err::Ptr{jpeg_error_mgr}
    mem::Ptr{jpeg_memory_mgr}
    progress::Ptr{jpeg_progress_mgr}
    client_data::Ptr{Cvoid}
    is_decompressor::boolean
    global_state::Cint
    src::Ptr{jpeg_source_mgr}
    image_width::JDIMENSION
    image_height::JDIMENSION
    num_components::Cint
    jpeg_color_space::J_COLOR_SPACE
    out_color_space::J_COLOR_SPACE
    scale_num::Cuint
    scale_denom::Cuint
    output_gamma::Cdouble
    buffered_image::boolean
    raw_data_out::boolean
    dct_method::J_DCT_METHOD
    do_fancy_upsampling::boolean
    do_block_smoothing::boolean
    quantize_colors::boolean
    dither_mode::J_DITHER_MODE
    two_pass_quantize::boolean
    desired_number_of_colors::Cint
    enable_1pass_quant::boolean
    enable_external_quant::boolean
    enable_2pass_quant::boolean
    output_width::JDIMENSION
    output_height::JDIMENSION
    out_color_components::Cint
    output_components::Cint
    rec_outbuf_height::Cint
    actual_number_of_colors::Cint
    colormap::JSAMPARRAY
    output_scanline::JDIMENSION
    input_scan_number::Cint
    input_iMCU_row::JDIMENSION
    output_scan_number::Cint
    output_iMCU_row::JDIMENSION
    coef_bits::Ptr{NTuple{64, Cint}}
    quant_tbl_ptrs::NTuple{4, Ptr{JQUANT_TBL}}
    dc_huff_tbl_ptrs::NTuple{4, Ptr{JHUFF_TBL}}
    ac_huff_tbl_ptrs::NTuple{4, Ptr{JHUFF_TBL}}
    data_precision::Cint
    comp_info::Ptr{jpeg_component_info}
    is_baseline::boolean
    progressive_mode::boolean
    arith_code::boolean
    arith_dc_L::NTuple{16, UINT8}
    arith_dc_U::NTuple{16, UINT8}
    arith_ac_K::NTuple{16, UINT8}
    restart_interval::Cuint
    saw_JFIF_marker::boolean
    JFIF_major_version::UINT8
    JFIF_minor_version::UINT8
    density_unit::UINT8
    X_density::UINT16
    Y_density::UINT16
    saw_Adobe_marker::boolean
    Adobe_transform::UINT8
    CCIR601_sampling::boolean
    marker_list::jpeg_saved_marker_ptr
    max_h_samp_factor::Cint
    max_v_samp_factor::Cint
    min_DCT_h_scaled_size::Cint
    min_DCT_v_scaled_size::Cint
    total_iMCU_rows::JDIMENSION
    sample_range_limit::Ptr{JSAMPLE}
    comps_in_scan::Cint
    cur_comp_info::NTuple{4, Ptr{jpeg_component_info}}
    MCUs_per_row::JDIMENSION
    MCU_rows_in_scan::JDIMENSION
    blocks_in_MCU::Cint
    MCU_membership::NTuple{10, Cint}
    Ss::Cint
    Se::Cint
    Ah::Cint
    Al::Cint
    block_size::Cint
    natural_order::Ptr{Cint}
    lim_Se::Cint
    unread_marker::Cint
    master::Ptr{jpeg_decomp_master}
    main::Ptr{jpeg_d_main_controller}
    coef::Ptr{jpeg_d_coef_controller}
    post::Ptr{jpeg_d_post_controller}
    inputctl::Ptr{jpeg_input_controller}
    marker::Ptr{jpeg_marker_reader}
    entropy::Ptr{jpeg_entropy_decoder}
    idct::Ptr{jpeg_inverse_dct}
    upsample::Ptr{jpeg_upsampler}
    cconvert::Ptr{jpeg_color_deconverter}
    cquantize::Ptr{jpeg_color_quantizer}
    jpeg_decompress_struct() = new()
end
function Base.getproperty(x::Ptr{jpeg_decompress_struct}, f::Symbol)
    f === :err && return Ptr{Ptr{jpeg_error_mgr}}(x + 0)
    f === :mem && return Ptr{Ptr{jpeg_memory_mgr}}(x + 8)
    f === :progress && return Ptr{Ptr{jpeg_progress_mgr}}(x + 16)
    f === :client_data && return Ptr{Ptr{Cvoid}}(x + 24)
    f === :is_decompressor && return Ptr{boolean}(x + 32)
    f === :global_state && return Ptr{Cint}(x + 36)
    f === :src && return Ptr{Ptr{jpeg_source_mgr}}(x + 40)
    f === :image_width && return Ptr{JDIMENSION}(x + 48)
    f === :image_height && return Ptr{JDIMENSION}(x + 52)
    f === :num_components && return Ptr{Cint}(x + 56)
    f === :jpeg_color_space && return Ptr{J_COLOR_SPACE}(x + 60)
    f === :out_color_space && return Ptr{J_COLOR_SPACE}(x + 64)
    f === :scale_num && return Ptr{Cuint}(x + 68)
    f === :scale_denom && return Ptr{Cuint}(x + 72)
    f === :output_gamma && return Ptr{Cdouble}(x + 80)
    f === :buffered_image && return Ptr{boolean}(x + 88)
    f === :raw_data_out && return Ptr{boolean}(x + 92)
    f === :dct_method && return Ptr{J_DCT_METHOD}(x + 96)
    f === :do_fancy_upsampling && return Ptr{boolean}(x + 100)
    f === :do_block_smoothing && return Ptr{boolean}(x + 104)
    f === :quantize_colors && return Ptr{boolean}(x + 108)
    f === :dither_mode && return Ptr{J_DITHER_MODE}(x + 112)
    f === :two_pass_quantize && return Ptr{boolean}(x + 116)
    f === :desired_number_of_colors && return Ptr{Cint}(x + 120)
    f === :enable_1pass_quant && return Ptr{boolean}(x + 124)
    f === :enable_external_quant && return Ptr{boolean}(x + 128)
    f === :enable_2pass_quant && return Ptr{boolean}(x + 132)
    f === :output_width && return Ptr{JDIMENSION}(x + 136)
    f === :output_height && return Ptr{JDIMENSION}(x + 140)
    f === :out_color_components && return Ptr{Cint}(x + 144)
    f === :output_components && return Ptr{Cint}(x + 148)
    f === :rec_outbuf_height && return Ptr{Cint}(x + 152)
    f === :actual_number_of_colors && return Ptr{Cint}(x + 156)
    f === :colormap && return Ptr{JSAMPARRAY}(x + 160)
    f === :output_scanline && return Ptr{JDIMENSION}(x + 168)
    f === :input_scan_number && return Ptr{Cint}(x + 172)
    f === :input_iMCU_row && return Ptr{JDIMENSION}(x + 176)
    f === :output_scan_number && return Ptr{Cint}(x + 180)
    f === :output_iMCU_row && return Ptr{JDIMENSION}(x + 184)
    f === :coef_bits && return Ptr{Ptr{NTuple{64, Cint}}}(x + 192)
    f === :quant_tbl_ptrs && return Ptr{NTuple{4, Ptr{JQUANT_TBL}}}(x + 200)
    f === :dc_huff_tbl_ptrs && return Ptr{NTuple{4, Ptr{JHUFF_TBL}}}(x + 232)
    f === :ac_huff_tbl_ptrs && return Ptr{NTuple{4, Ptr{JHUFF_TBL}}}(x + 264)
    f === :data_precision && return Ptr{Cint}(x + 296)
    f === :comp_info && return Ptr{Ptr{jpeg_component_info}}(x + 304)
    f === :is_baseline && return Ptr{boolean}(x + 312)
    f === :progressive_mode && return Ptr{boolean}(x + 316)
    f === :arith_code && return Ptr{boolean}(x + 320)
    f === :arith_dc_L && return Ptr{NTuple{16, UINT8}}(x + 324)
    f === :arith_dc_U && return Ptr{NTuple{16, UINT8}}(x + 340)
    f === :arith_ac_K && return Ptr{NTuple{16, UINT8}}(x + 356)
    f === :restart_interval && return Ptr{Cuint}(x + 372)
    f === :saw_JFIF_marker && return Ptr{boolean}(x + 376)
    f === :JFIF_major_version && return Ptr{UINT8}(x + 380)
    f === :JFIF_minor_version && return Ptr{UINT8}(x + 381)
    f === :density_unit && return Ptr{UINT8}(x + 382)
    f === :X_density && return Ptr{UINT16}(x + 384)
    f === :Y_density && return Ptr{UINT16}(x + 386)
    f === :saw_Adobe_marker && return Ptr{boolean}(x + 388)
    f === :Adobe_transform && return Ptr{UINT8}(x + 392)
    f === :CCIR601_sampling && return Ptr{boolean}(x + 396)
    f === :marker_list && return Ptr{jpeg_saved_marker_ptr}(x + 400)
    f === :max_h_samp_factor && return Ptr{Cint}(x + 408)
    f === :max_v_samp_factor && return Ptr{Cint}(x + 412)
    f === :min_DCT_h_scaled_size && return Ptr{Cint}(x + 416)
    f === :min_DCT_v_scaled_size && return Ptr{Cint}(x + 420)
    f === :total_iMCU_rows && return Ptr{JDIMENSION}(x + 424)
    f === :sample_range_limit && return Ptr{Ptr{JSAMPLE}}(x + 432)
    f === :comps_in_scan && return Ptr{Cint}(x + 440)
    f === :cur_comp_info && return Ptr{NTuple{4, Ptr{jpeg_component_info}}}(x + 448)
    f === :MCUs_per_row && return Ptr{JDIMENSION}(x + 480)
    f === :MCU_rows_in_scan && return Ptr{JDIMENSION}(x + 484)
    f === :blocks_in_MCU && return Ptr{Cint}(x + 488)
    f === :MCU_membership && return Ptr{NTuple{10, Cint}}(x + 492)
    f === :Ss && return Ptr{Cint}(x + 532)
    f === :Se && return Ptr{Cint}(x + 536)
    f === :Ah && return Ptr{Cint}(x + 540)
    f === :Al && return Ptr{Cint}(x + 544)
    f === :block_size && return Ptr{Cint}(x + 548)
    f === :natural_order && return Ptr{Ptr{Cint}}(x + 552)
    f === :lim_Se && return Ptr{Cint}(x + 560)
    f === :unread_marker && return Ptr{Cint}(x + 564)
    f === :master && return Ptr{Ptr{jpeg_decomp_master}}(x + 568)
    f === :main && return Ptr{Ptr{jpeg_d_main_controller}}(x + 576)
    f === :coef && return Ptr{Ptr{jpeg_d_coef_controller}}(x + 584)
    f === :post && return Ptr{Ptr{jpeg_d_post_controller}}(x + 592)
    f === :inputctl && return Ptr{Ptr{jpeg_input_controller}}(x + 600)
    f === :marker && return Ptr{Ptr{jpeg_marker_reader}}(x + 608)
    f === :entropy && return Ptr{Ptr{jpeg_entropy_decoder}}(x + 616)
    f === :idct && return Ptr{Ptr{jpeg_inverse_dct}}(x + 624)
    f === :upsample && return Ptr{Ptr{jpeg_upsampler}}(x + 632)
    f === :cconvert && return Ptr{Ptr{jpeg_color_deconverter}}(x + 640)
    f === :cquantize && return Ptr{Ptr{jpeg_color_quantizer}}(x + 648)
    return getfield(x, f)
end

function Base.setproperty!(x::Ptr{jpeg_decompress_struct}, f::Symbol, v)
    unsafe_store!(getproperty(x, f), v)
end


const jvirt_sarray_control = Cvoid

const jvirt_sarray_ptr = Ptr{jvirt_sarray_control}

const jvirt_barray_control = Cvoid

const jvirt_barray_ptr = Ptr{jvirt_barray_control}

# typedef boolean ( * jpeg_marker_parser_method ) ( j_decompress_ptr cinfo )
const jpeg_marker_parser_method = Ptr{Cvoid}

function jpeg_std_error(err)
    ccall((:jpeg_std_error, libjpeg), Ptr{jpeg_error_mgr}, (Ptr{jpeg_error_mgr},), err)
end

function jpeg_destroy_compress(cinfo)
    ccall((:jpeg_destroy_compress, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_destroy_decompress(cinfo)
    ccall((:jpeg_destroy_decompress, libjpeg), Cvoid, (j_decompress_ptr,), cinfo)
end

function jpeg_stdio_dest(cinfo, outfile)
    ccall((:jpeg_stdio_dest, libjpeg), Cvoid, (j_compress_ptr, Ptr{Libc.FILE}), cinfo, outfile)
end

function jpeg_stdio_src(cinfo, infile)
    ccall((:jpeg_stdio_src, libjpeg), Cvoid, (j_decompress_ptr, Ptr{Libc.FILE}), cinfo, infile)
end

function jpeg_mem_dest(cinfo, outbuffer, outsize)
    ccall((:jpeg_mem_dest, libjpeg), Cvoid, (j_compress_ptr, Ptr{Ptr{Cuchar}}, Ptr{Culong}), cinfo, outbuffer, outsize)
end

function jpeg_mem_src(cinfo, inbuffer, insize)
    ccall((:jpeg_mem_src, libjpeg), Cvoid, (j_decompress_ptr, Ptr{Cuchar}, Culong), cinfo, inbuffer, insize)
end

function jpeg_set_defaults(cinfo)
    ccall((:jpeg_set_defaults, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_set_colorspace(cinfo, colorspace)
    ccall((:jpeg_set_colorspace, libjpeg), Cvoid, (j_compress_ptr, J_COLOR_SPACE), cinfo, colorspace)
end

function jpeg_default_colorspace(cinfo)
    ccall((:jpeg_default_colorspace, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_set_quality(cinfo, quality, force_baseline)
    ccall((:jpeg_set_quality, libjpeg), Cvoid, (j_compress_ptr, Cint, boolean), cinfo, quality, force_baseline)
end

function jpeg_set_linear_quality(cinfo, scale_factor, force_baseline)
    ccall((:jpeg_set_linear_quality, libjpeg), Cvoid, (j_compress_ptr, Cint, boolean), cinfo, scale_factor, force_baseline)
end

function jpeg_default_qtables(cinfo, force_baseline)
    ccall((:jpeg_default_qtables, libjpeg), Cvoid, (j_compress_ptr, boolean), cinfo, force_baseline)
end

function jpeg_add_quant_table(cinfo, which_tbl, basic_table, scale_factor, force_baseline)
    ccall((:jpeg_add_quant_table, libjpeg), Cvoid, (j_compress_ptr, Cint, Ptr{Cuint}, Cint, boolean), cinfo, which_tbl, basic_table, scale_factor, force_baseline)
end

function jpeg_quality_scaling(quality)
    ccall((:jpeg_quality_scaling, libjpeg), Cint, (Cint,), quality)
end

function jpeg_enable_lossless(cinfo, predictor_selection_value, point_transform)
    ccall((:jpeg_enable_lossless, libjpeg), Cvoid, (j_compress_ptr, Cint, Cint), cinfo, predictor_selection_value, point_transform)
end

function jpeg_simple_progression(cinfo)
    ccall((:jpeg_simple_progression, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_suppress_tables(cinfo, suppress)
    ccall((:jpeg_suppress_tables, libjpeg), Cvoid, (j_compress_ptr, boolean), cinfo, suppress)
end

function jpeg_alloc_quant_table(cinfo)
    ccall((:jpeg_alloc_quant_table, libjpeg), Ptr{JQUANT_TBL}, (j_common_ptr,), cinfo)
end

function jpeg_alloc_huff_table(cinfo)
    ccall((:jpeg_alloc_huff_table, libjpeg), Ptr{JHUFF_TBL}, (j_common_ptr,), cinfo)
end

function jpeg_start_compress(cinfo, write_all_tables)
    ccall((:jpeg_start_compress, libjpeg), Cvoid, (j_compress_ptr, boolean), cinfo, write_all_tables)
end

function jpeg_write_scanlines(cinfo, scanlines, num_lines)
    ccall((:jpeg_write_scanlines, libjpeg), JDIMENSION, (j_compress_ptr, JSAMPARRAY, JDIMENSION), cinfo, scanlines, num_lines)
end

function jpeg12_write_scanlines(cinfo, scanlines, num_lines)
    ccall((:jpeg12_write_scanlines, libjpeg), JDIMENSION, (j_compress_ptr, J12SAMPARRAY, JDIMENSION), cinfo, scanlines, num_lines)
end

function jpeg16_write_scanlines(cinfo, scanlines, num_lines)
    ccall((:jpeg16_write_scanlines, libjpeg), JDIMENSION, (j_compress_ptr, J16SAMPARRAY, JDIMENSION), cinfo, scanlines, num_lines)
end

function jpeg_finish_compress(cinfo)
    ccall((:jpeg_finish_compress, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_calc_jpeg_dimensions(cinfo)
    ccall((:jpeg_calc_jpeg_dimensions, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_write_raw_data(cinfo, data, num_lines)
    ccall((:jpeg_write_raw_data, libjpeg), JDIMENSION, (j_compress_ptr, JSAMPIMAGE, JDIMENSION), cinfo, data, num_lines)
end

function jpeg12_write_raw_data(cinfo, data, num_lines)
    ccall((:jpeg12_write_raw_data, libjpeg), JDIMENSION, (j_compress_ptr, J12SAMPIMAGE, JDIMENSION), cinfo, data, num_lines)
end

function jpeg_write_marker(cinfo, marker, dataptr, datalen)
    ccall((:jpeg_write_marker, libjpeg), Cvoid, (j_compress_ptr, Cint, Ptr{JOCTET}, Cuint), cinfo, marker, dataptr, datalen)
end

function jpeg_write_m_header(cinfo, marker, datalen)
    ccall((:jpeg_write_m_header, libjpeg), Cvoid, (j_compress_ptr, Cint, Cuint), cinfo, marker, datalen)
end

function jpeg_write_m_byte(cinfo, val)
    ccall((:jpeg_write_m_byte, libjpeg), Cvoid, (j_compress_ptr, Cint), cinfo, val)
end

function jpeg_write_tables(cinfo)
    ccall((:jpeg_write_tables, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_write_icc_profile(cinfo, icc_data_ptr, icc_data_len)
    ccall((:jpeg_write_icc_profile, libjpeg), Cvoid, (j_compress_ptr, Ptr{JOCTET}, Cuint), cinfo, icc_data_ptr, icc_data_len)
end

function jpeg_read_header(cinfo, require_image)
    ccall((:jpeg_read_header, libjpeg), Cint, (j_decompress_ptr, boolean), cinfo, require_image)
end

function jpeg_start_decompress(cinfo)
    ccall((:jpeg_start_decompress, libjpeg), boolean, (j_decompress_ptr,), cinfo)
end

function jpeg_read_scanlines(cinfo, scanlines, max_lines)
    ccall((:jpeg_read_scanlines, libjpeg), JDIMENSION, (j_decompress_ptr, JSAMPARRAY, JDIMENSION), cinfo, scanlines, max_lines)
end

function jpeg12_read_scanlines(cinfo, scanlines, max_lines)
    ccall((:jpeg12_read_scanlines, libjpeg), JDIMENSION, (j_decompress_ptr, J12SAMPARRAY, JDIMENSION), cinfo, scanlines, max_lines)
end

function jpeg16_read_scanlines(cinfo, scanlines, max_lines)
    ccall((:jpeg16_read_scanlines, libjpeg), JDIMENSION, (j_decompress_ptr, J16SAMPARRAY, JDIMENSION), cinfo, scanlines, max_lines)
end

function jpeg_skip_scanlines(cinfo, num_lines)
    ccall((:jpeg_skip_scanlines, libjpeg), JDIMENSION, (j_decompress_ptr, JDIMENSION), cinfo, num_lines)
end

function jpeg12_skip_scanlines(cinfo, num_lines)
    ccall((:jpeg12_skip_scanlines, libjpeg), JDIMENSION, (j_decompress_ptr, JDIMENSION), cinfo, num_lines)
end

function jpeg_crop_scanline(cinfo, xoffset, width)
    ccall((:jpeg_crop_scanline, libjpeg), Cvoid, (j_decompress_ptr, Ptr{JDIMENSION}, Ptr{JDIMENSION}), cinfo, xoffset, width)
end

function jpeg12_crop_scanline(cinfo, xoffset, width)
    ccall((:jpeg12_crop_scanline, libjpeg), Cvoid, (j_decompress_ptr, Ptr{JDIMENSION}, Ptr{JDIMENSION}), cinfo, xoffset, width)
end

function jpeg_finish_decompress(cinfo)
    ccall((:jpeg_finish_decompress, libjpeg), boolean, (j_decompress_ptr,), cinfo)
end

function jpeg_read_raw_data(cinfo, data, max_lines)
    ccall((:jpeg_read_raw_data, libjpeg), JDIMENSION, (j_decompress_ptr, JSAMPIMAGE, JDIMENSION), cinfo, data, max_lines)
end

function jpeg12_read_raw_data(cinfo, data, max_lines)
    ccall((:jpeg12_read_raw_data, libjpeg), JDIMENSION, (j_decompress_ptr, J12SAMPIMAGE, JDIMENSION), cinfo, data, max_lines)
end

function jpeg_has_multiple_scans(cinfo)
    ccall((:jpeg_has_multiple_scans, libjpeg), boolean, (j_decompress_ptr,), cinfo)
end

function jpeg_start_output(cinfo, scan_number)
    ccall((:jpeg_start_output, libjpeg), boolean, (j_decompress_ptr, Cint), cinfo, scan_number)
end

function jpeg_finish_output(cinfo)
    ccall((:jpeg_finish_output, libjpeg), boolean, (j_decompress_ptr,), cinfo)
end

function jpeg_input_complete(cinfo)
    ccall((:jpeg_input_complete, libjpeg), boolean, (j_decompress_ptr,), cinfo)
end

function jpeg_new_colormap(cinfo)
    ccall((:jpeg_new_colormap, libjpeg), Cvoid, (j_decompress_ptr,), cinfo)
end

function jpeg_consume_input(cinfo)
    ccall((:jpeg_consume_input, libjpeg), Cint, (j_decompress_ptr,), cinfo)
end

function jpeg_core_output_dimensions(cinfo)
    ccall((:jpeg_core_output_dimensions, libjpeg), Cvoid, (j_decompress_ptr,), cinfo)
end

function jpeg_calc_output_dimensions(cinfo)
    ccall((:jpeg_calc_output_dimensions, libjpeg), Cvoid, (j_decompress_ptr,), cinfo)
end

function jpeg_save_markers(cinfo, marker_code, length_limit)
    ccall((:jpeg_save_markers, libjpeg), Cvoid, (j_decompress_ptr, Cint, Cuint), cinfo, marker_code, length_limit)
end

function jpeg_set_marker_processor(cinfo, marker_code, routine)
    ccall((:jpeg_set_marker_processor, libjpeg), Cvoid, (j_decompress_ptr, Cint, jpeg_marker_parser_method), cinfo, marker_code, routine)
end

function jpeg_read_coefficients(cinfo)
    ccall((:jpeg_read_coefficients, libjpeg), Ptr{jvirt_barray_ptr}, (j_decompress_ptr,), cinfo)
end

function jpeg_write_coefficients(cinfo, coef_arrays)
    ccall((:jpeg_write_coefficients, libjpeg), Cvoid, (j_compress_ptr, Ptr{jvirt_barray_ptr}), cinfo, coef_arrays)
end

function jpeg_copy_critical_parameters(srcinfo, dstinfo)
    ccall((:jpeg_copy_critical_parameters, libjpeg), Cvoid, (j_decompress_ptr, j_compress_ptr), srcinfo, dstinfo)
end

function jpeg_abort_compress(cinfo)
    ccall((:jpeg_abort_compress, libjpeg), Cvoid, (j_compress_ptr,), cinfo)
end

function jpeg_abort_decompress(cinfo)
    ccall((:jpeg_abort_decompress, libjpeg), Cvoid, (j_decompress_ptr,), cinfo)
end

function jpeg_abort(cinfo)
    ccall((:jpeg_abort, libjpeg), Cvoid, (j_common_ptr,), cinfo)
end

function jpeg_destroy(cinfo)
    ccall((:jpeg_destroy, libjpeg), Cvoid, (j_common_ptr,), cinfo)
end

function jpeg_resync_to_restart(cinfo, desired)
    ccall((:jpeg_resync_to_restart, libjpeg), boolean, (j_decompress_ptr, Cint), cinfo, desired)
end

function jpeg_read_icc_profile(cinfo, icc_data_ptr, icc_data_len)
    ccall((:jpeg_read_icc_profile, libjpeg), boolean, (j_decompress_ptr, Ptr{Ptr{JOCTET}}, Ptr{Cuint}), cinfo, icc_data_ptr, icc_data_len)
end

@cenum TJINIT::UInt32 begin
    TJINIT_COMPRESS = 0
    TJINIT_DECOMPRESS = 1
    TJINIT_TRANSFORM = 2
end

@cenum TJSAMP::Int32 begin
    TJSAMP_444 = 0
    TJSAMP_422 = 1
    TJSAMP_420 = 2
    TJSAMP_GRAY = 3
    TJSAMP_440 = 4
    TJSAMP_411 = 5
    TJSAMP_441 = 6
    TJSAMP_UNKNOWN = -1
end

@cenum TJPF::Int32 begin
    TJPF_RGB = 0
    TJPF_BGR = 1
    TJPF_RGBX = 2
    TJPF_BGRX = 3
    TJPF_XBGR = 4
    TJPF_XRGB = 5
    TJPF_GRAY = 6
    TJPF_RGBA = 7
    TJPF_BGRA = 8
    TJPF_ABGR = 9
    TJPF_ARGB = 10
    TJPF_CMYK = 11
    TJPF_UNKNOWN = -1
end

@cenum TJCS::UInt32 begin
    TJCS_RGB = 0
    TJCS_YCbCr = 1
    TJCS_GRAY = 2
    TJCS_CMYK = 3
    TJCS_YCCK = 4
end

@cenum TJPARAM::UInt32 begin
    TJPARAM_STOPONWARNING = 0
    TJPARAM_BOTTOMUP = 1
    TJPARAM_NOREALLOC = 2
    TJPARAM_QUALITY = 3
    TJPARAM_SUBSAMP = 4
    TJPARAM_JPEGWIDTH = 5
    TJPARAM_JPEGHEIGHT = 6
    TJPARAM_PRECISION = 7
    TJPARAM_COLORSPACE = 8
    TJPARAM_FASTUPSAMPLE = 9
    TJPARAM_FASTDCT = 10
    TJPARAM_OPTIMIZE = 11
    TJPARAM_PROGRESSIVE = 12
    TJPARAM_SCANLIMIT = 13
    TJPARAM_ARITHMETIC = 14
    TJPARAM_LOSSLESS = 15
    TJPARAM_LOSSLESSPSV = 16
    TJPARAM_LOSSLESSPT = 17
    TJPARAM_RESTARTBLOCKS = 18
    TJPARAM_RESTARTROWS = 19
    TJPARAM_XDENSITY = 20
    TJPARAM_YDENSITY = 21
    TJPARAM_DENSITYUNITS = 22
end

@cenum TJERR::UInt32 begin
    TJERR_WARNING = 0
    TJERR_FATAL = 1
end

@cenum TJXOP::UInt32 begin
    TJXOP_NONE = 0
    TJXOP_HFLIP = 1
    TJXOP_VFLIP = 2
    TJXOP_TRANSPOSE = 3
    TJXOP_TRANSVERSE = 4
    TJXOP_ROT90 = 5
    TJXOP_ROT180 = 6
    TJXOP_ROT270 = 7
end

mutable struct tjscalingfactor
    num::Cint
    denom::Cint
    tjscalingfactor() = new()
end

mutable struct tjregion
    x::Cint
    y::Cint
    w::Cint
    h::Cint
    tjregion() = new()
end

struct tjtransform
    r::tjregion
    op::Cint
    options::Cint
    data::Ptr{Cvoid}
    customFilter::Ptr{Cvoid}
end

const tjhandle = Ptr{Cvoid}

function tj3Init(initType)
    ccall((:tj3Init, libturbojpeg), tjhandle, (Cint,), initType)
end

function tj3Set(handle, param, value)
    ccall((:tj3Set, libturbojpeg), Cint, (tjhandle, Cint, Cint), handle, param, value)
end

function tj3Get(handle, param)
    ccall((:tj3Get, libturbojpeg), Cint, (tjhandle, Cint), handle, param)
end

function tj3Compress8(handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
    ccall((:tj3Compress8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}), handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
end

function tj3Compress12(handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
    ccall((:tj3Compress12, libturbojpeg), Cint, (tjhandle, Ptr{Cshort}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}), handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
end

function tj3Compress16(handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
    ccall((:tj3Compress16, libturbojpeg), Cint, (tjhandle, Ptr{Cushort}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}), handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize)
end

function tj3CompressFromYUV8(handle, srcBuf, width, align, height, jpegBuf, jpegSize)
    ccall((:tj3CompressFromYUV8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}), handle, srcBuf, width, align, height, jpegBuf, jpegSize)
end

function tj3CompressFromYUVPlanes8(handle, srcPlanes, width, strides, height, jpegBuf, jpegSize)
    ccall((:tj3CompressFromYUVPlanes8, libturbojpeg), Cint, (tjhandle, Ptr{Ptr{Cuchar}}, Cint, Ptr{Cint}, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}), handle, srcPlanes, width, strides, height, jpegBuf, jpegSize)
end

function tj3JPEGBufSize(width, height, jpegSubsamp)
    ccall((:tj3JPEGBufSize, libturbojpeg), Csize_t, (Cint, Cint, Cint), width, height, jpegSubsamp)
end

function tj3YUVBufSize(width, align, height, subsamp)
    ccall((:tj3YUVBufSize, libturbojpeg), Csize_t, (Cint, Cint, Cint, Cint), width, align, height, subsamp)
end

function tj3YUVPlaneSize(componentID, width, stride, height, subsamp)
    ccall((:tj3YUVPlaneSize, libturbojpeg), Csize_t, (Cint, Cint, Cint, Cint, Cint), componentID, width, stride, height, subsamp)
end

function tj3YUVPlaneWidth(componentID, width, subsamp)
    ccall((:tj3YUVPlaneWidth, libturbojpeg), Cint, (Cint, Cint, Cint), componentID, width, subsamp)
end

function tj3YUVPlaneHeight(componentID, height, subsamp)
    ccall((:tj3YUVPlaneHeight, libturbojpeg), Cint, (Cint, Cint, Cint), componentID, height, subsamp)
end

function tj3EncodeYUV8(handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, align)
    ccall((:tj3EncodeYUV8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Cuchar}, Cint), handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, align)
end

function tj3EncodeYUVPlanes8(handle, srcBuf, width, pitch, height, pixelFormat, dstPlanes, strides)
    ccall((:tj3EncodeYUVPlanes8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Cint}), handle, srcBuf, width, pitch, height, pixelFormat, dstPlanes, strides)
end

function tj3DecompressHeader(handle, jpegBuf, jpegSize)
    ccall((:tj3DecompressHeader, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t), handle, jpegBuf, jpegSize)
end

function tj3GetScalingFactors(numScalingFactors)
    ccall((:tj3GetScalingFactors, libturbojpeg), Ptr{tjscalingfactor}, (Ptr{Cint},), numScalingFactors)
end

function tj3SetScalingFactor(handle, scalingFactor)
    ccall((:tj3SetScalingFactor, libturbojpeg), Cint, (tjhandle, tjscalingfactor), handle, scalingFactor)
end

function tj3SetCroppingRegion(handle, croppingRegion)
    ccall((:tj3SetCroppingRegion, libturbojpeg), Cint, (tjhandle, tjregion), handle, croppingRegion)
end

function tj3Decompress8(handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
    ccall((:tj3Decompress8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Ptr{Cuchar}, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
end

function tj3Decompress12(handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
    ccall((:tj3Decompress12, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Ptr{Cshort}, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
end

function tj3Decompress16(handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
    ccall((:tj3Decompress16, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Ptr{Cushort}, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, pitch, pixelFormat)
end

function tj3DecompressToYUV8(handle, jpegBuf, jpegSize, dstBuf, align)
    ccall((:tj3DecompressToYUV8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Ptr{Cuchar}, Cint), handle, jpegBuf, jpegSize, dstBuf, align)
end

function tj3DecompressToYUVPlanes8(handle, jpegBuf, jpegSize, dstPlanes, strides)
    ccall((:tj3DecompressToYUVPlanes8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Ptr{Ptr{Cuchar}}, Ptr{Cint}), handle, jpegBuf, jpegSize, dstPlanes, strides)
end

function tj3DecodeYUV8(handle, srcBuf, align, dstBuf, width, pitch, height, pixelFormat)
    ccall((:tj3DecodeYUV8, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Ptr{Cuchar}, Cint, Cint, Cint, Cint), handle, srcBuf, align, dstBuf, width, pitch, height, pixelFormat)
end

function tj3DecodeYUVPlanes8(handle, srcPlanes, strides, dstBuf, width, pitch, height, pixelFormat)
    ccall((:tj3DecodeYUVPlanes8, libturbojpeg), Cint, (tjhandle, Ptr{Ptr{Cuchar}}, Ptr{Cint}, Ptr{Cuchar}, Cint, Cint, Cint, Cint), handle, srcPlanes, strides, dstBuf, width, pitch, height, pixelFormat)
end

function tj3Transform(handle, jpegBuf, jpegSize, n, dstBufs, dstSizes, transforms)
    ccall((:tj3Transform, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Csize_t, Cint, Ptr{Ptr{Cuchar}}, Ptr{Csize_t}, Ptr{tjtransform}), handle, jpegBuf, jpegSize, n, dstBufs, dstSizes, transforms)
end

function tj3Destroy(handle)
    ccall((:tj3Destroy, libturbojpeg), Cvoid, (tjhandle,), handle)
end

function tj3Alloc(bytes)
    ccall((:tj3Alloc, libturbojpeg), Ptr{Cvoid}, (Csize_t,), bytes)
end

function tj3LoadImage8(handle, filename, width, align, height, pixelFormat)
    ccall((:tj3LoadImage8, libturbojpeg), Ptr{Cuchar}, (tjhandle, Ptr{Cchar}, Ptr{Cint}, Cint, Ptr{Cint}, Ptr{Cint}), handle, filename, width, align, height, pixelFormat)
end

function tj3LoadImage12(handle, filename, width, align, height, pixelFormat)
    ccall((:tj3LoadImage12, libturbojpeg), Ptr{Cshort}, (tjhandle, Ptr{Cchar}, Ptr{Cint}, Cint, Ptr{Cint}, Ptr{Cint}), handle, filename, width, align, height, pixelFormat)
end

function tj3LoadImage16(handle, filename, width, align, height, pixelFormat)
    ccall((:tj3LoadImage16, libturbojpeg), Ptr{Cushort}, (tjhandle, Ptr{Cchar}, Ptr{Cint}, Cint, Ptr{Cint}, Ptr{Cint}), handle, filename, width, align, height, pixelFormat)
end

function tj3SaveImage8(handle, filename, buffer, width, pitch, height, pixelFormat)
    ccall((:tj3SaveImage8, libturbojpeg), Cint, (tjhandle, Ptr{Cchar}, Ptr{Cuchar}, Cint, Cint, Cint, Cint), handle, filename, buffer, width, pitch, height, pixelFormat)
end

function tj3SaveImage12(handle, filename, buffer, width, pitch, height, pixelFormat)
    ccall((:tj3SaveImage12, libturbojpeg), Cint, (tjhandle, Ptr{Cchar}, Ptr{Cshort}, Cint, Cint, Cint, Cint), handle, filename, buffer, width, pitch, height, pixelFormat)
end

function tj3SaveImage16(handle, filename, buffer, width, pitch, height, pixelFormat)
    ccall((:tj3SaveImage16, libturbojpeg), Cint, (tjhandle, Ptr{Cchar}, Ptr{Cushort}, Cint, Cint, Cint, Cint), handle, filename, buffer, width, pitch, height, pixelFormat)
end

function tj3Free(buffer)
    ccall((:tj3Free, libturbojpeg), Cvoid, (Ptr{Cvoid},), buffer)
end

function tj3GetErrorStr(handle)
    ccall((:tj3GetErrorStr, libturbojpeg), Ptr{Cchar}, (tjhandle,), handle)
end

function tj3GetErrorCode(handle)
    ccall((:tj3GetErrorCode, libturbojpeg), Cint, (tjhandle,), handle)
end

function TJBUFSIZE(width, height)
    ccall((:TJBUFSIZE, libturbojpeg), Culong, (Cint, Cint), width, height)
end

function tjCompress(handle, srcBuf, width, pitch, height, pixelSize, dstBuf, compressedSize, jpegSubsamp, jpegQual, flags)
    ccall((:tjCompress, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Cuchar}, Ptr{Culong}, Cint, Cint, Cint), handle, srcBuf, width, pitch, height, pixelSize, dstBuf, compressedSize, jpegSubsamp, jpegQual, flags)
end

function tjDecompress(handle, jpegBuf, jpegSize, dstBuf, width, pitch, height, pixelSize, flags)
    ccall((:tjDecompress, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, width, pitch, height, pixelSize, flags)
end

function tjDecompressHeader(handle, jpegBuf, jpegSize, width, height)
    ccall((:tjDecompressHeader, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cint}, Ptr{Cint}), handle, jpegBuf, jpegSize, width, height)
end

function tjDestroy(handle)
    ccall((:tjDestroy, libturbojpeg), Cint, (tjhandle,), handle)
end

function tjGetErrorStr()
    ccall((:tjGetErrorStr, libturbojpeg), Ptr{Cchar}, ())
end

function tjInitCompress()
    ccall((:tjInitCompress, libturbojpeg), tjhandle, ())
end

function tjInitDecompress()
    ccall((:tjInitDecompress, libturbojpeg), tjhandle, ())
end

function TJBUFSIZEYUV(width, height, jpegSubsamp)
    ccall((:TJBUFSIZEYUV, libturbojpeg), Culong, (Cint, Cint, Cint), width, height, jpegSubsamp)
end

function tjDecompressHeader2(handle, jpegBuf, jpegSize, width, height, jpegSubsamp)
    ccall((:tjDecompressHeader2, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cint}, Ptr{Cint}, Ptr{Cint}), handle, jpegBuf, jpegSize, width, height, jpegSubsamp)
end

function tjDecompressToYUV(handle, jpegBuf, jpegSize, dstBuf, flags)
    ccall((:tjDecompressToYUV, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cuchar}, Cint), handle, jpegBuf, jpegSize, dstBuf, flags)
end

function tjEncodeYUV(handle, srcBuf, width, pitch, height, pixelSize, dstBuf, subsamp, flags)
    ccall((:tjEncodeYUV, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Cuchar}, Cint, Cint), handle, srcBuf, width, pitch, height, pixelSize, dstBuf, subsamp, flags)
end

function tjAlloc(bytes)
    ccall((:tjAlloc, libturbojpeg), Ptr{Cuchar}, (Cint,), bytes)
end

function tjBufSize(width, height, jpegSubsamp)
    ccall((:tjBufSize, libturbojpeg), Culong, (Cint, Cint, Cint), width, height, jpegSubsamp)
end

function tjBufSizeYUV(width, height, subsamp)
    ccall((:tjBufSizeYUV, libturbojpeg), Culong, (Cint, Cint, Cint), width, height, subsamp)
end

function tjCompress2(handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize, jpegSubsamp, jpegQual, flags)
    ccall((:tjCompress2, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Culong}, Cint, Cint, Cint), handle, srcBuf, width, pitch, height, pixelFormat, jpegBuf, jpegSize, jpegSubsamp, jpegQual, flags)
end

function tjDecompress2(handle, jpegBuf, jpegSize, dstBuf, width, pitch, height, pixelFormat, flags)
    ccall((:tjDecompress2, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, width, pitch, height, pixelFormat, flags)
end

function tjEncodeYUV2(handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, subsamp, flags)
    ccall((:tjEncodeYUV2, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Cuchar}, Cint, Cint), handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, subsamp, flags)
end

function tjFree(buffer)
    ccall((:tjFree, libturbojpeg), Cvoid, (Ptr{Cuchar},), buffer)
end

function tjGetScalingFactors(numscalingfactors)
    ccall((:tjGetScalingFactors, libturbojpeg), Ptr{tjscalingfactor}, (Ptr{Cint},), numscalingfactors)
end

function tjInitTransform()
    ccall((:tjInitTransform, libturbojpeg), tjhandle, ())
end

function tjTransform(handle, jpegBuf, jpegSize, n, dstBufs, dstSizes, transforms, flags)
    ccall((:tjTransform, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Cint, Ptr{Ptr{Cuchar}}, Ptr{Culong}, Ptr{tjtransform}, Cint), handle, jpegBuf, jpegSize, n, dstBufs, dstSizes, transforms, flags)
end

function tjBufSizeYUV2(width, align, height, subsamp)
    ccall((:tjBufSizeYUV2, libturbojpeg), Culong, (Cint, Cint, Cint, Cint), width, align, height, subsamp)
end

function tjCompressFromYUV(handle, srcBuf, width, align, height, subsamp, jpegBuf, jpegSize, jpegQual, flags)
    ccall((:tjCompressFromYUV, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Culong}, Cint, Cint), handle, srcBuf, width, align, height, subsamp, jpegBuf, jpegSize, jpegQual, flags)
end

function tjCompressFromYUVPlanes(handle, srcPlanes, width, strides, height, subsamp, jpegBuf, jpegSize, jpegQual, flags)
    ccall((:tjCompressFromYUVPlanes, libturbojpeg), Cint, (tjhandle, Ptr{Ptr{Cuchar}}, Cint, Ptr{Cint}, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Culong}, Cint, Cint), handle, srcPlanes, width, strides, height, subsamp, jpegBuf, jpegSize, jpegQual, flags)
end

function tjDecodeYUV(handle, srcBuf, align, subsamp, dstBuf, width, pitch, height, pixelFormat, flags)
    ccall((:tjDecodeYUV, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Cint), handle, srcBuf, align, subsamp, dstBuf, width, pitch, height, pixelFormat, flags)
end

function tjDecodeYUVPlanes(handle, srcPlanes, strides, subsamp, dstBuf, width, pitch, height, pixelFormat, flags)
    ccall((:tjDecodeYUVPlanes, libturbojpeg), Cint, (tjhandle, Ptr{Ptr{Cuchar}}, Ptr{Cint}, Cint, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Cint), handle, srcPlanes, strides, subsamp, dstBuf, width, pitch, height, pixelFormat, flags)
end

function tjDecompressHeader3(handle, jpegBuf, jpegSize, width, height, jpegSubsamp, jpegColorspace)
    ccall((:tjDecompressHeader3, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cint}, Ptr{Cint}, Ptr{Cint}, Ptr{Cint}), handle, jpegBuf, jpegSize, width, height, jpegSubsamp, jpegColorspace)
end

function tjDecompressToYUV2(handle, jpegBuf, jpegSize, dstBuf, width, align, height, flags)
    ccall((:tjDecompressToYUV2, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Cuchar}, Cint, Cint, Cint, Cint), handle, jpegBuf, jpegSize, dstBuf, width, align, height, flags)
end

function tjDecompressToYUVPlanes(handle, jpegBuf, jpegSize, dstPlanes, width, strides, height, flags)
    ccall((:tjDecompressToYUVPlanes, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Culong, Ptr{Ptr{Cuchar}}, Cint, Ptr{Cint}, Cint, Cint), handle, jpegBuf, jpegSize, dstPlanes, width, strides, height, flags)
end

function tjEncodeYUV3(handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, align, subsamp, flags)
    ccall((:tjEncodeYUV3, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Cuchar}, Cint, Cint, Cint), handle, srcBuf, width, pitch, height, pixelFormat, dstBuf, align, subsamp, flags)
end

function tjEncodeYUVPlanes(handle, srcBuf, width, pitch, height, pixelFormat, dstPlanes, strides, subsamp, flags)
    ccall((:tjEncodeYUVPlanes, libturbojpeg), Cint, (tjhandle, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Ptr{Ptr{Cuchar}}, Ptr{Cint}, Cint, Cint), handle, srcBuf, width, pitch, height, pixelFormat, dstPlanes, strides, subsamp, flags)
end

function tjPlaneHeight(componentID, height, subsamp)
    ccall((:tjPlaneHeight, libturbojpeg), Cint, (Cint, Cint, Cint), componentID, height, subsamp)
end

function tjPlaneSizeYUV(componentID, width, stride, height, subsamp)
    ccall((:tjPlaneSizeYUV, libturbojpeg), Culong, (Cint, Cint, Cint, Cint, Cint), componentID, width, stride, height, subsamp)
end

function tjPlaneWidth(componentID, width, subsamp)
    ccall((:tjPlaneWidth, libturbojpeg), Cint, (Cint, Cint, Cint), componentID, width, subsamp)
end

function tjGetErrorCode(handle)
    ccall((:tjGetErrorCode, libturbojpeg), Cint, (tjhandle,), handle)
end

function tjGetErrorStr2(handle)
    ccall((:tjGetErrorStr2, libturbojpeg), Ptr{Cchar}, (tjhandle,), handle)
end

function tjLoadImage(filename, width, align, height, pixelFormat, flags)
    ccall((:tjLoadImage, libturbojpeg), Ptr{Cuchar}, (Ptr{Cchar}, Ptr{Cint}, Cint, Ptr{Cint}, Ptr{Cint}, Cint), filename, width, align, height, pixelFormat, flags)
end

function tjSaveImage(filename, buffer, width, pitch, height, pixelFormat, flags)
    ccall((:tjSaveImage, libturbojpeg), Cint, (Ptr{Cchar}, Ptr{Cuchar}, Cint, Cint, Cint, Cint, Cint), filename, buffer, width, pitch, height, pixelFormat, flags)
end

const JPEG_LIB_VERSION = 80

const LIBJPEG_TURBO_VERSION_NUMBER = 3000001

const C_ARITH_CODING_SUPPORTED = 1

const D_ARITH_CODING_SUPPORTED = 1

const MEM_SRCDST_SUPPORTED = 1

const WITH_SIMD = 1

const BITS_IN_JSAMPLE = 8

const MAX_COMPONENTS = 10

const MAXJSAMPLE = 255

const CENTERJSAMPLE = 128

const MAXJ12SAMPLE = 4095

const CENTERJ12SAMPLE = 2048

const MAXJ16SAMPLE = 65535

const CENTERJ16SAMPLE = 32768

const JPEG_MAX_DIMENSION = Clong(65500)

const FAR = nothing

const FALSE = 0

const TRUE = 1

const DCTSIZE = 8

const DCTSIZE2 = 64

const NUM_QUANT_TBLS = 4

const NUM_HUFF_TBLS = 4

const NUM_ARITH_TBLS = 16

const MAX_COMPS_IN_SCAN = 4

const MAX_SAMP_FACTOR = 4

const C_MAX_BLOCKS_IN_MCU = 10

const D_MAX_BLOCKS_IN_MCU = 10

const JCS_EXTENSIONS = 1

const JCS_ALPHA_EXTENSIONS = 1

const JDCT_DEFAULT = JDCT_ISLOW

const JDCT_FASTEST = JDCT_IFAST

# Skipping MacroDefinition: jpeg_common_fields struct jpeg_error_mgr * err ; /* Error handler module */ struct jpeg_memory_mgr * mem ; /* Memory manager module */ struct jpeg_progress_mgr * progress ; /* Progress monitor, or NULL if none */ void * client_data ; /* Available for use by application */ boolean is_decompressor ; /* So common code can tell which is which */ int global_state

const JMSG_LENGTH_MAX = 200

const JMSG_STR_PARM_MAX = 80

const JPOOL_PERMANENT = 0

const JPOOL_IMAGE = 1

const JPOOL_NUMPOOLS = 2

const JPEG_SUSPENDED = 0

const JPEG_HEADER_OK = 1

const JPEG_HEADER_TABLES_ONLY = 2

const JPEG_REACHED_SOS = 1

const JPEG_REACHED_EOI = 2

const JPEG_ROW_COMPLETED = 3

const JPEG_SCAN_COMPLETED = 4

const JPEG_RST0 = 0xd0

const JPEG_EOI = 0xd9

const JPEG_APP0 = 0xe0

const JPEG_COM = 0xfe

const __TURBOJPEG_H__ = nothing

const DLLEXPORT = nothing

const DLLCALL = nothing

const TJ_NUMINIT = 3

const TJ_NUMSAMP = 7

const TJ_NUMPF = 12

const TJ_NUMCS = 5

const TJ_NUMPARAM = nothing

const TJ_NUMERR = 2

const TJ_NUMXOP = 8

const TJXOPT_PERFECT = 1 << 0

const TJXOPT_TRIM = 1 << 1

const TJXOPT_CROP = 1 << 2

const TJXOPT_GRAY = 1 << 3

const TJXOPT_NOOUTPUT = 1 << 4

const TJXOPT_PROGRESSIVE = 1 << 5

const TJXOPT_COPYNONE = 1 << 6

const TJXOPT_ARITHMETIC = 1 << 7

const TJXOPT_OPTIMIZE = 1 << 8

const NUMSUBOPT = TJ_NUMSAMP

const TJ_444 = TJSAMP_444

const TJ_422 = TJSAMP_422

const TJ_420 = TJSAMP_420

const TJ_411 = TJSAMP_420

const TJ_GRAYSCALE = TJSAMP_GRAY

const TJ_BGR = 1

const TJFLAG_BOTTOMUP = 2

const TJ_BOTTOMUP = TJFLAG_BOTTOMUP

const TJFLAG_FORCEMMX = 8

const TJ_FORCEMMX = TJFLAG_FORCEMMX

const TJFLAG_FORCESSE = 16

const TJ_FORCESSE = TJFLAG_FORCESSE

const TJFLAG_FORCESSE2 = 32

const TJ_FORCESSE2 = TJFLAG_FORCESSE2

const TJ_ALPHAFIRST = 64

const TJFLAG_FORCESSE3 = 128

const TJ_FORCESSE3 = TJFLAG_FORCESSE3

const TJFLAG_FASTUPSAMPLE = 256

const TJ_FASTUPSAMPLE = TJFLAG_FASTUPSAMPLE

const TJ_YUV = 512

const TJFLAG_NOREALLOC = 1024

const TJFLAG_FASTDCT = 2048

const TJFLAG_ACCURATEDCT = 4096

const TJFLAG_STOPONWARNING = 8192

const TJFLAG_PROGRESSIVE = 16384

const TJFLAG_LIMITSCANS = 32768

######################################################################################################
# macros from jpeglib.h

jpeg_create_compress(cinfo) =
    jpeg_CreateCompress(cinfo, JPEG_LIB_VERSION, sizeof(jpeg_compress_struct))
jpeg_create_decompress(cinfo) =
    jpeg_CreateDecompress(cinfo, JPEG_LIB_VERSION, sizeof(jpeg_decompress_struct))


end # module
