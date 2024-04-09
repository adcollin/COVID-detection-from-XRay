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

# Function to randomly sample one-tenth of the files
random_sample() {
    files=("$@")
    num_files=${#files[@]}
    sample_size=$((num_files / 10))
    sampled_files=($(shuf -e "${files[@]}" | head -n $sample_size))
    echo "${sampled_files[@]}"
}

directory="$1"
output_directory="$2"

# Get all DICOM files in the directory
dicom_files=("$directory"/*.dcm)

# Randomly sample one-tenth of the DICOM files
sampled_files=($(random_sample "${dicom_files[@]}"))

# Convert sampled pbm files to PNG format
for file in "${sampled_files[@]}"; do
    if [ -f "$file" ]; then
        convert_to_png "$file" "$output_directory"
    fi
done

echo "Conversion complete."
