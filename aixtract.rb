#!/usr/bin/env ruby

require 'fileutils'
require 'time'

# Get the project name from the current directory
project_name = File.basename Dir.pwd

# Create target directory with timestamp
timestamp = Time.now.strftime '%Y%m%d_%H%M%S'
target_dir = File.expand_path "~/Downloads/#{project_name}_#{timestamp}"
FileUtils.mkdir_p target_dir

# Read .aixtract file
begin
  File.readlines('.aixtract').each do |filepath|
    # Clean the filepath (remove newlines and any surrounding whitespace)
    filepath = filepath.strip

    next if filepath.empty?

    # Skip commented lines
    next if filepath.start_with?('#')

    begin
      if File.exist? filepath
        # Convert path separators to double underscores
        new_filename = filepath.gsub '/', '__'

        # Copy the file to the target directory with the new name
        FileUtils.cp(filepath, File.join(target_dir, new_filename))
        puts "Copied: #{filepath} -> #{new_filename}"
      else
        puts "Warning: File not found: #{filepath}"
      end
    rescue => e
      puts "Error processing #{filepath}: #{e.message}"
    end
  end

  puts "\nFiles extracted to: #{target_dir}"
  puts "Total files processed: #{Dir.glob(File.join(target_dir, '*')).count}"
rescue Errno::ENOENT
  puts "Error: .aixtract file not found in current directory"
  exit 1
rescue => e
  puts "Error: #{e.message}"
  exit 1
end
