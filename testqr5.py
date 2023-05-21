import csv
import cv2
from pyzbar import pyzbar
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class QRCodeScannerApp(App):
    camera = None
    capture = None
    csv_file = None
    csv_writer = None

    def on_start(self):
       
        self.csv_file = open('abcde.csv', 'a+', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        

       
        self.camera = cv2.VideoCapture(0)
        self.capture = self.camera.isOpened()
        self.schedule = Clock.schedule_interval(lambda dt: self.scan_qr_code(dt, self.csv_writer), 1.0 / 0.5)

    def on_stop(self):
        
        if self.capture:
            self.schedule.cancel()
            self.camera.release()
        if self.csv_file:
            self.csv_file.close()

    def scan_qr_code(self, dt, csv_writer):
        ret, frame = self.camera.read()
        frame = cv2.flip(frame, 0)

        if ret:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            
            barcodes = pyzbar.decode(gray)

            
            for barcode in barcodes:
                
                (x, y, w, h) = barcode.rect

                
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

               
                barcode_data = barcode.data.decode("utf-8")
                barcode_data2 = "Present"
                barcode_type = barcode.type

               
                print(f"{barcode_data}")

               
                x = 'Present'
                csv_writer.writerow([barcode_data, barcode_type, x])

            
            self.image_widget.texture = self._convert_frame_to_texture(frame)

    def _convert_frame_to_texture(self, frame):
       
        buf = frame.tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        return texture

    def build(self):
       
        layout = BoxLayout(orientation='vertical')

        
        self.image_widget = Image()

       
        layout.add_widget(self.image_widget)

        
        close_button = Button(text='Close the App')
        close_button.bind(on_release=self.close_app)

       
        layout.add_widget(close_button)

        return layout

    def close_app(self, instance):
        
        App.get_running_app().stop()


if __name__ == '__main__':
    QRCodeScannerApp().run()
