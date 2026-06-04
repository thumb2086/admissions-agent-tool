"""共用 PPTX 產生引擎 — 提供所有 layout helper 函式"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
import os

# 預設色票
C_DARK = RGBColor(0x1A, 0x27, 0x3F)
C_BLUE = RGBColor(0x2B, 0x57, 0x9A)
C_WHITE = RGBColor(255, 255, 255)
C_GRAY = RGBColor(0x88, 0x88, 0x88)
C_TEXT = RGBColor(0x33, 0x33, 0x33)
C_LIGHT = RGBColor(0xF0, 0xF4, 0xF8)
C_HIGHLIGHT_BG = RGBColor(0xE8, 0xEE, 0xF5)

# 預設字型
FONT_NAME = "微軟正黑體"


def new_presentation(width_inches=13.333, height_inches=7.5):
    """建立新簡報，預設寬螢幕比例"""
    prs = Presentation()
    prs.slide_width = Inches(width_inches)
    prs.slide_height = Inches(height_inches)
    return prs


def set_background(slide, color):
    """設定投影片背景色"""
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height, text, font_size=18, bold=False, color=C_TEXT, font_name=FONT_NAME, alignment=PP_ALIGN.LEFT, word_wrap=True):
    """加入文字方塊（單行）"""
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_multiline_text(slide, left, top, width, height, lines, font_size=14, color=C_TEXT, font_name=FONT_NAME, line_spacing=4):
    """加入多行文字方塊"""
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = font_name
        p.space_after = Pt(line_spacing)
    return txBox


def add_image(slide, image_path, left, top, width, height=None, rotation=0):
    """加入圖片，若檔案不存在則不處理"""
    if not os.path.exists(image_path):
        print(f"[WARN] 圖片不存在: {image_path}")
        return None
    try:
        pic = slide.shapes.add_picture(image_path, Inches(left), Inches(top), Inches(width))
        if height:
            pic.height = Inches(height)
        if rotation:
            pic.rotation = rotation
        return pic
    except Exception as e:
        print(f"[ERROR] 圖片載入失敗 {image_path}: {e}")
        return None


def add_rect(slide, left, top, width, height, fill_color=C_BLUE, corner_radius=None):
    """加入矩形/圓角矩形背景"""
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if corner_radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(shape_type, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape


def add_line(slide, left, top, width, color=C_BLUE):
    """加入分隔線"""
    ln = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(0.04))
    ln.fill.solid()
    ln.fill.fore_color.rgb = color
    ln.line.fill.background()


def add_box_with_text(slide, left, top, width, height, fill_color, text, font_size=18, font_color=C_WHITE, bold=True, font_name=FONT_NAME):
    """加入圓角矩形 + 文字"""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = font_color
    p.font.bold = bold
    p.font.name = font_name
    return shape


def add_cover(slide, title_text, subtitle_text=""):
    """封面頁（深色背景）"""
    set_background(slide, C_DARK)
    add_textbox(slide, 1, 2.5, 11, 1.5, title_text, 44, True, C_WHITE)
    add_line(slide, 1, 4.2, 3.5, C_BLUE)
    if subtitle_text:
        add_textbox(slide, 1, 4.6, 11, 0.8, subtitle_text, 22, False, RGBColor(0xBB, 0xCC, 0xDD))


def add_title(slide, section_title):
    """章節標題頁（白色背景 + 藍色底線）"""
    set_background(slide, C_WHITE)
    add_textbox(slide, 0.8, 0.3, 11, 0.8, section_title, 32, True, C_DARK)
    add_line(slide, 0.8, 1.2, 11.5, C_BLUE)


def add_toc(slide, items, highlight_text="", photo_path=None):
    """目錄頁：items=[(編號, 標題, 副標題), ...]"""
    set_background(slide, C_WHITE)
    add_textbox(slide, 0.8, 0.3, 11, 0.8, "目　錄", 32, True, C_DARK)
    add_line(slide, 0.8, 1.2, 4, C_BLUE)

    y = 1.55
    for num, title, subtitle in items:
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), Inches(y + 0.02), Inches(0.4), Inches(0.4))
        circle.fill.solid()
        circle.fill.fore_color.rgb = C_BLUE
        circle.line.fill.background()
        tf = circle.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.text = num
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.font.name = FONT_NAME
        p.alignment = PP_ALIGN.CENTER

        add_textbox(slide, 1.4, y, 7, 0.35, title, 16, True, C_TEXT, word_wrap=False)
        if subtitle:
            add_textbox(slide, 1.4, y + 0.32, 7, 0.3, subtitle, 12, False, C_GRAY, word_wrap=False)
        y += 0.65

    if highlight_text:
        bx = add_rect(slide, 0.8, y + 0.15, 6, 0.4, C_HIGHLIGHT_BG, corner_radius=True)
        add_textbox(slide, 1.0, y + 0.2, 5.6, 0.3, highlight_text, 12, True, C_BLUE)

    if photo_path:
        add_image(slide, photo_path, 8.0, 1.6, 4.5)


def add_ending(slide, text="謝謝觀看"):
    """結尾頁（深色背景）"""
    set_background(slide, C_DARK)
    add_textbox(slide, 1, 2.8, 11, 1.5, text, 44, True, C_WHITE)
    add_line(slide, 1, 4.5, 3.5, C_BLUE)


def add_footer(prs, footer_text="", total_only=False):
    """為所有投影片加入頁尾 + 頁碼（封面除外）"""
    total = len(prs.slides)
    for idx, slide in enumerate(prs.slides):
        if footer_text:
            add_textbox(slide, 0.5, 7.1, 6, 0.3, footer_text, 10, False, C_GRAY)
        if idx > 0:
            add_textbox(slide, 12.0, 7.1, 1.2, 0.3, f"{idx+1}/{total}", 9, False, C_GRAY)


def add_pie_chart(slide, left, top, width, height, categories, values, series_name="佔比"):
    """加入圓餅圖"""
    chart_data = CategoryChartData()
    chart_data.categories = categories
    chart_data.add_series(series_name, values)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.PIE, Inches(left), Inches(top), Inches(width), Inches(height),
        chart_data
    ).chart
    chart.has_legend = True
    chart.legend.include_in_layout = False
    chart.legend.font.size = Pt(12)
    chart.legend.position = 2
    plot = chart.plots[0]
    plot.has_data_labels = True
    data_labels = plot.data_labels
    data_labels.show_percentage = True
    data_labels.show_value = False
    data_labels.show_category_name = True
    data_labels.show_leader_lines = True
    data_labels.font.size = Pt(13)
    data_labels.font.bold = True
    data_labels.font.color.rgb = C_TEXT
    return chart


def add_image_grid(slide, images, x_positions, y_positions, width, height=None):
    """以 2D 網格放置多張圖片"""
    for i, img_path in enumerate(images):
        if not img_path:
            continue
        col = i % len(x_positions)
        row = i // len(x_positions)
        if row < len(y_positions):
            add_image(slide, img_path, x_positions[col], y_positions[row], width, height)
