#!/bin/bash

# Function to convert DICOM files to PNG format
convert_to_png() {
    file="$1"
    output_dir="$2"
    pgm_file="${file%.*}.pgm"
    dctopgm8 "$file" -quiet > "$pgm_file"
    convert "$pgm_file" "${output_dir}/${file##*/}.png"
    echo "Converted $file to ${output_dir}/${file##*/}.png"
    rm "$pgm_file"
}

# Function to randomly sample some of the files if the size of too big
random_sample() {
    files=("$@")
    num_files=${#files[@]}
    sample_size=$((num_files / 2))
    sampled_files=($(shuf -e "${files[@]}" | head -n $sample_size))
    echo "${sampled_files[@]}"
}

directory="$1"
output_directory="$2"

# Get all DICOM files in the directory
dicom_files=("$directory"/*.dcm)

# Randomly sample one-tenth of the DICOM files
#sampled_files=($(random_sample "${dicom_files[@]}"))

# Convert sampled pbm files to PNG format
for file in "${dicom_files[@]}"; do
    if [ -f "$file" ]; then
        convert_to_png "$file" "$output_directory"
    fi
done

#Compress the images to limit the size of the local directory
mogrify -resize 224x224 -quality 75 ${output_dir}/*.png

#Run the pre-processing python script to convert to numpy
#python preprocessing.py 

echo "Conversion complete."
