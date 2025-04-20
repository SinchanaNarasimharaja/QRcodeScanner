"""
QR Code Scanner in Python using OpenCV and pyzbar

Dependencies:
- opencv-python
- pyzbar

You can install the dependencies using:
pip install opencv-python pyzbar

This program captures video from the webcam, detects QR codes in real-time,
and displays the decoded data on the video feed.
"""

import cv2
from pyzbar import pyzbar

def decode_qr_codes(frame):
    # Decode QR codes in the frame
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # Draw rectangle around the QR code
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points, returnPoints=True)
            points = hull.reshape(-1, 2)
        n = len(points)
        for j in range(n):
            cv2.line(frame, points[j], points[(j + 1) % n], (0, 255, 0), 3)

        # Put decoded text above the rectangle
        qr_data = obj.data.decode("utf-8")
        qr_type = obj.type
        text = f"{qr_data} ({qr_type})"
        cv2.putText(frame, text, (points[0].x, points[0].y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        print(f"Decoded {qr_type}: {qr_data}")

    return frame

def main():
    # Open webcam video stream
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting QR code scanner. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decode QR codes in the frame
        frame = decode_qr_codes(frame)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
