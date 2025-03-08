//______________________________________________________________________
//______________________________________________________________________
//      _   __   _   _ _   _   _   _         _
// |   |_| | _  | | | V | | | | / |_/ |_| | /
// |__ | | |__| |_| |   | |_| | \ |   | | | \_
//  _  _         _ ___  _       _ ___   _                     / /
// /  | | |\ |  \   |  | / | | /   |   \                     (^^)
// \_ |_| | \| _/   |  | \ |_| \_  |  _/                     (____)o
//______________________________________________________________________
//______________________________________________________________________
//
//----------------------------------------------------------------------
// Copyright 2024, Rebecca Rashkin
// -------------------------------
// This code may be copied, redistributed, transformed, or built
// upon in any format for educational, non-commercial purposes.
//
// Please give me appropriate credit should you choose to use this
// resource. Thank you :)
//----------------------------------------------------------------------
//
//______________________________________________________________________
// //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
//______________________________________________________________________
// DESCRIPTION
// Contains code to generate two half sheets printed on one 8.5 x 11
// letter size sheet of paper. Accounts for a 1/2 left margin for
// binding
//______________________________________________________________________

//______________________________________________________________________
// CONSTANTS
//______________________________________________________________________
// Note: This file uses constants from an external file. The html that
// calls this script should first list the constants file before
// listing this file.
//______________________________________________________________________

const letter_wdth_landscape_in  = 11;
const letter_hght_landscape_in  = 8.5;

const letter_wdth_landscape_px  = DPI * letter_wdth_landscape_in;
const letter_hght_landscape_px  = DPI * letter_hght_landscape_in;

//______________________________________________________________________
// Margins
//______________________________________________________________________

// To account for left binding
const std_margin_in     = 0.25;
const binder_margin_in  = 0.5;

const t_margin_in       = std_margin_in;
const r_margin_in       = std_margin_in;
const b_margin_in       = std_margin_in;

let l_margin_in       = 0;

// Change margin sides depending on double-sided print
if (DOUBLE_SIDED)
{
  l_margin_in       = std_margin_in;
}
else
{
  l_margin_in       = binder_margin_in;
}

// Convert in to px
const std_margin_px     = std_margin_in     * DPI;
const binder_margin_px  = binder_margin_in  * DPI;

const l_margin_px = l_margin_in * DPI;
const r_margin_px = r_margin_in * DPI;
const t_margin_px = t_margin_in * DPI;
const b_margin_px = b_margin_in * DPI;

//______________________________________________________________________
// Content Dimensions
//______________________________________________________________________

// Width of middle column that serves as margin
// Will account for two binder margins if printing double sided
let mid_margin_wdth = 0;

if (DOUBLE_SIDED)
{
  mid_margin_wdth = 2 * binder_margin_px;
}
else
{
  mid_margin_wdth = l_margin_px + r_margin_px;
}

// Create whole letter
let letter_size_div = document.createElement("div");
letter_size_div.style.width   = letter_wdth_landscape_px + "px";
letter_size_div.style.height  = letter_hght_landscape_px + "px";
letter_size_div.style.border  = DEBUG0_BORDER_STYLE;

let letter_content_div = document.createElement("div");
letter_content_div.style.width  = "100%";
letter_content_div.style.height = "100%";
letter_content_div.style.border = DEBUG0_BORDER_STYLE;

// Set content margins through padding
letter_size_div.style.margin        = "0px";
letter_size_div.style.paddingTop    = t_margin_px + "px";
letter_size_div.style.paddingBottom = b_margin_px + "px";
letter_size_div.style.paddingLeft   = l_margin_px + "px";
letter_size_div.style.paddingRight  = r_margin_px + "px";

document.getElementById("content-container")
  .appendChild(letter_size_div);

letter_size_div.appendChild(letter_content_div);

let content_table = document.createElement("table");
let content_row   = document.createElement("tr");

let l_content_box = document.createElement("td");
let m_margin_box  = document.createElement("td");
let r_content_box = document.createElement("td");

letter_content_div.appendChild(content_table);

content_table.appendChild(content_row);
content_row.appendChild(l_content_box);
content_row.appendChild(m_margin_box);
content_row.appendChild(r_content_box);

content_table.style.height = "100%";
content_row.style.height = "100%";

content_table.style.width = "100%";
l_content_box.style.width = "auto";
 m_margin_box.style.width  = mid_margin_wdth + "px";
r_content_box.style.width = "auto";

content_table.style.border = DEBUG1_BORDER_STYLE;
l_content_box.style.border = CONTENT_BORDER_STYLE;
m_margin_box.style.border  = DEBUG1_BORDER_STYLE;
r_content_box.style.border = CONTENT_BORDER_STYLE;

l_content_box.style.padding = "0px";
m_margin_box.style.padding  = "0px";
r_content_box.style.padding = "0px";
