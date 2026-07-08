import sys
import os

# FIX: Force dummy streams if Windows suppresses the console window
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')
if sys.stdin is None:
    sys.stdin = open(os.devnull, 'r')

# --- YOUR ORIGINAL CODE STARTS HERE ---
import threading
import tkinter as tk
import customtkinter as ctk
import speedtest
# ... (rest of your script remains exactly the same)

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FastSpeedTestApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fast Desktop Speedtest")
        self.geometry("450x550")
        self.resizable(False, False)

        # 1. Header Logo (Fast.com style)
        self.logo_label = ctk.CTkLabel(self, text="FAST", font=("Helvetica", 32, "bold"), text_color="#E50914")
        self.logo_label.pack(pady=(40, 5))
        
        self.sub_label = ctk.CTkLabel(self, text="Internet Speed Test", font=("Helvetica", 13), text_color="gray")
        self.sub_label.pack(pady=(0, 30))

        # 2. Main Metric Display
        self.speed_label = ctk.CTkLabel(self, text="--", font=("Helvetica", 86, "bold"), text_color="white")
        self.speed_label.pack()

        self.unit_label = ctk.CTkLabel(self, text="Mbps", font=("Helvetica", 18), text_color="gray")
        self.unit_label.pack(pady=(0, 20))

        # 3. Status/Progress Info
        self.status_label = ctk.CTkLabel(self, text="Click the icon below to start", font=("Helvetica", 14, "italic"), text_color="#A0A0A0")
        self.status_label.pack(pady=10)

        # 4. Speedometer Action Button (The "Icon")
        # We use a clean Unicode character (⚡ or 💨) inside a circular button frame
        self.action_btn = ctk.CTkButton(
            self, 
            text="⚡", 
            font=("Helvetica", 36), 
            width=90, 
            height=90, 
            corner_radius=45, # Makes it a perfect circle
            fg_color="#2B2B2B", 
            hover_color="#E50914", 
            command=self.start_speed_test
        )
        self.action_btn.pack(pady=20)

        # 5. Detail Metrics Panel (Hidden initially)
        self.metrics_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        self.ping_label = ctk.CTkLabel(self.metrics_frame, text="Ping: --", font=("Helvetica", 14), text_color="gray")
        self.ping_label.grid(row=0, column=0, padx=25)
        
        self.upload_label = ctk.CTkLabel(self.metrics_frame, text="Upload: --", font=("Helvetica", 14), text_color="gray")
        self.upload_label.grid(row=0, column=1, padx=25)

    def start_speed_test(self):
        # UI State reset
        self.action_btn.configure(state="disabled", fg_color="#1F1F1F", text="⏳")
        self.metrics_frame.pack_forget()
        self.speed_label.configure(text="--", text_color="#A0A0A0")
        
        # Offload network requests to background thread to avoid app freezing
        threading.Thread(target=self.run_network_logic, daemon=True).start()

    def run_network_logic(self):
        try:
            self.status_label.configure(text="Finding best server...")
            st = speedtest.Speedtest()
            st.get_best_server()

            # Measure Download
            self.status_label.configure(text="Testing Download speed...")
            download_raw = st.download()
            download_mbps = download_raw / 1_000_000 # Convert bits to Megabits
            
            # Show download speed instantly in big text
            self.speed_label.configure(text=f"{download_mbps:.1f}", text_color="white")

            # Measure Upload
            self.status_label.configure(text="Testing Upload speed...")
            upload_raw = st.upload()
            upload_mbps = upload_raw / 1_000_000

            # Collect results
            results = st.results.dict()
            ping = results["ping"]

            # Update final UI elements safely
            self.ping_label.configure(text=f"Ping: {ping:.0f} ms")
            self.upload_label.configure(text=f"Upload: {upload_mbps:.1f} Mbps")
            
            self.status_label.configure(text="Test complete!")
            self.metrics_frame.pack(pady=15)

        except Exception as e:
            self.status_label.configure(text="Error connecting to test server.")
            self.speed_label.configure(text="Err")
        
        finally:
            # Re-enable the button for another run
            self.action_btn.configure(state="normal", fg_color="#2B2B2B", text="⚡")

if __name__ == "__main__":
    app = FastSpeedTestApp()
    app.mainloop()