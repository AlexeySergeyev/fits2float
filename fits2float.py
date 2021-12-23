# %%
from astropy.io import fits
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from time import sleep
import numpy as np

# %%

def convert(files):
    for file in files:
        hdu = fits.open(file, mode='update')
        if (not 'CONVER' in hdu[0].header):
            if hdu[0].header['BITPIX'] > 0:
                hdu[0].header['CONVERT'] = True
                data = np.asarray(hdu[0].data, dtype=float)
                data[np.where(data < 0)] += 65536
                hdu[0].data = data.astype(np.float32)

                hdu.flush()
                hdu.close()

                sleep(1)
        print(file)

# %%
# files = None
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=100)
canvas.grid(columnspan=1, rowspan=2)

instruct = tk.Label(root, text='Select fits files to convert')
instruct.grid(columnspan=3, column=0, row=0)

def openfiles():
    # print('works')
    # global files
    files = askopenfilenames(initialdir='/home/asergeyev/code/python/gls_search/images/des_known/DES0049-1749/DESJ005027.7920-174009.4800/', 
            title='Select fits files',
            filetypes=[('Fits files', ('.fit', '.fits')),
                ('all files', '.*'),
           ])
    # print(files)
    convert(files)

btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, 
                command=lambda:openfiles(),
                bg='#20bebe', fg='white')
btn_text.set('Open')
btn.grid(column=0, row=1)

root.mainloop()
 # %%
