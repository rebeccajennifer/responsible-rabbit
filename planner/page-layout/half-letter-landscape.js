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

const letter_wdth_lndscp_in  = 11;
const letter_hght_lndscp_in  = 8.5;

const letter_wdth_lndscp_px  = DPI * letter_wdth_lndscp_in;
const letter_hght_lndscp_px  = DPI * letter_hght_lndscp_in;

let half_letter_layout = document.createElement("table");
half_letter_layout.style.width   = letter_wdth_lndscp_px + "px";
half_letter_layout.style.height  = letter_hght_lndscp_px + "px";
//______________________________________________________________________
// Debug
//______________________________________________________________________
// half_letter_layout.style.border  = CONTENT_BORDER_STYLE;
//______________________________________________________________________

document.getElementById("table-container")
  .appendChild(half_letter_layout);

const half_letter_wdth_lndscp_px  = letter_wdth_lndscp_px * 0.5;
const half_letter_hght_lndscp_px  = letter_hght_lndscp_px * 0.5;

//______________________________________________________________________
// Margins
//______________________________________________________________________

// To account for left binding
const l_margin_in     = 0.5;
const std_margin_in   = 0.25;
const r_margin_in     = std_margin_in;
const t_margin_in     = std_margin_in;
const b_margin_in     = std_margin_in;

const l_margin_px   = l_margin_in   * DPI;
const std_margin_px = std_margin_in * DPI;
const r_margin_px   = r_margin_in   * DPI;
const t_margin_px   = t_margin_in   * DPI;
const b_margin_px   = b_margin_in   * DPI;

//______________________________________________________________________
// Content Dimensions
//______________________________________________________________________
//
// |<------ 5.5in ------>|<------ 5.5in ------>|
//  0.5 left margin
//  -------------------------------------------
// |   ----------------  |   ----------------  |
// |  |                | |  |  ^             | |
// | o|                | | o|  |             | |
// |  |<- .5 left      | |  |  .25 top &     | |
// |  |     margin     | |  |     bottom     | |
// | o|                | | o|     margin     | |
// |  |    .25 right ->| |  |                | |
// |  |         margin | |  |                | |
// | o|                | | o|                | |
// |  |                | | ^|                | |
// |   ----------------  | | ----------------  |
//  -----------------------|-------------------
//                         holes for binding
//______________________________________________________________________

const content_size_wdth_px =
  half_letter_wdth_lndscp_px - l_margin_px - r_margin_px;

const content_size_hght_px =
  half_letter_hght_lndscp_px - t_margin_px - b_margin_px;

// Width of middle column that serves as margin
const mid_margin_width = l_margin_px + r_margin_px;
//______________________________________________________________________


let row = document.createElement("tr");

let left_content          = document.createElement("td");
left_content.style.width  = content_size_wdth_px + "px";

let right_content         = document.createElement("td");
right_content.style.width = content_size_wdth_px + "px";

let mid_margins           = document.createElement("td");
mid_margins.style.width   = mid_margin_width + "px";

half_letter_layout.style.padding  = "0px";
left_content.style.padding        = "0px";
right_content.style.padding       = "0px";
mid_margins.style.padding         = "0px";

left_content.style.border   = CONTENT_BORDER_STYLE;
right_content.style.border  = CONTENT_BORDER_STYLE;

row.appendChild(left_content);
row.appendChild(mid_margins);
row.appendChild(right_content);

half_letter_layout.style.borderCollapse = "collapse";
half_letter_layout.appendChild(row);