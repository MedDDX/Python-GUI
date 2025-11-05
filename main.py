from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: 0.05, 0.08, 0.13, 1

    canvas.before:
        Color:
            rgba: 0.06, 0.12, 0.20, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [0, 0, 300, 0]
        Color:
            rgba: 0.12, 0.18, 0.30, 0.8
        RoundedRectangle:
            pos: self.width * 0.55, -self.height * 0.15
            size: self.width * 0.6, self.height * 1.3
            radius: [300, 0, 0, 0]

    MDFloatLayout:
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(36)
            spacing: dp(20)
            size_hint: 0.55, None
            pos_hint: {"center_y": 0.58, "x": 0.05}

            MDLabel:
                text: "MedSim Diagnostics"
                font_style: "H3"
                adaptive_height: True
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Immerse yourself in a cinematic medical diagnosis simulation."
                font_style: "Subtitle1"
                adaptive_height: True
                theme_text_color: "Custom"
                text_color: 0.8, 0.87, 0.96, 1

            MDSeparator:
                height: dp(1)
                color: 0.2, 0.35, 0.5, 0.5

            MDBoxLayout:
                spacing: dp(20)
                adaptive_height: True

                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: dp(140), dp(160)
                    padding: dp(16)
                    radius: [22]
                    md_bg_color: 0.09, 0.14, 0.22, 0.95

                    MDIcon:
                        icon: "stethoscope"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.24, 0.70, 0.93, 1
                        font_size: "48sp"

                    MDLabel:
                        text: "Differentials"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        font_style: "Subtitle1"

                    MDLabel:
                        text: "Analyze evolving symptoms to narrow diagnoses."
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.7, 0.82, 0.95, 1
                        font_style: "Caption"

                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: dp(140), dp(160)
                    padding: dp(16)
                    radius: [22]
                    md_bg_color: 0.09, 0.14, 0.22, 0.95

                    MDIcon:
                        icon: "brain"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.39, 0.82, 0.68, 1
                        font_size: "48sp"

                    MDLabel:
                        text: "Consultations"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        font_style: "Subtitle1"

                    MDLabel:
                        text: "Collaborate with specialists and unlock insights."
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.7, 0.82, 0.95, 1
                        font_style: "Caption"

                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: dp(140), dp(160)
                    padding: dp(16)
                    radius: [22]
                    md_bg_color: 0.09, 0.14, 0.22, 0.95

                    MDIcon:
                        icon: "chart-bell-curve"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.94, 0.64, 0.33, 1
                        font_size: "48sp"

                    MDLabel:
                        text: "Outcomes"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        font_style: "Subtitle1"

                    MDLabel:
                        text: "Review patient arcs shaped by your decisions."
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.7, 0.82, 0.95, 1
                        font_style: "Caption"

            MDRaisedButton:
                text: "Enter Simulation"
                md_bg_color: 0.24, 0.70, 0.93, 1
                text_color: 0.05, 0.08, 0.13, 1
                pos_hint: {"x": 0, "center_y": 0.08}
                size_hint: None, None
                size: dp(220), dp(48)
                elevation: 0

        MDCard:
            size_hint: 0.32, 0.6
            pos_hint: {"center_y": 0.55, "right": 0.94}
            radius: [30]
            md_bg_color: 0.10, 0.16, 0.25, 0.95
            padding: dp(24)
            orientation: "vertical"
            spacing: dp(16)

            MDLabel:
                text: "Case Spotlight"
                font_style: "H5"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDSeparator:
                height: dp(1)
                color: 0.2, 0.35, 0.5, 0.5

            MDLabel:
                text: "A 29-year-old presents with intermittent chest pain and dizziness. Evaluate labs, imaging, and patient history to guide treatment."
                font_style: "Body2"
                theme_text_color: "Custom"
                text_color: 0.8, 0.87, 0.96, 1
                halign: "left"

            MDBoxLayout:
                adaptive_height: True
                spacing: dp(12)

                MDIcon:
                    icon: "clock-outline"
                    theme_text_color: "Custom"
                    text_color: 0.39, 0.82, 0.68, 1

                MDLabel:
                    text: "Estimated session: 15 min"
                    font_style: "Caption"
                    theme_text_color: "Custom"
                    text_color: 0.7, 0.82, 0.95, 1

            MDBoxLayout:
                adaptive_height: True
                spacing: dp(12)

                MDIcon:
                    icon: "account-group"
                    theme_text_color: "Custom"
                    text_color: 0.94, 0.64, 0.33, 1

                MDLabel:
                    text: "Collaborative team play"
                    font_style: "Caption"
                    theme_text_color: "Custom"
                    text_color: 0.7, 0.82, 0.95, 1
"""


class MedSimApp(MDApp):
    def build(self):
        self.title = "MedSim Diagnostics"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MedSimApp().run()
