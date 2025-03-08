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

// Pages will be printed double sided
// This value will affect margins
// 0: not double-sided
// 1: double-sided
const DOUBLE_SIDED          = 0;
const DPI = 96;

const STD_MARGIN_IN    = 0.3;
const BINDER_MARGIN_IN = 1;

const STD_MARGIN_PX    = STD_MARGIN_IN    * DPI;
const BINDER_MARGIN_PX = BINDER_MARGIN_IN * DPI;

const BORDER_WIDTH           = 1;
const DEBUG0_BORDER_STYLE    = `${BORDER_WIDTH}px solid #800080`;
const DEBUG1_BORDER_STYLE    = `${BORDER_WIDTH}px solid #008080`;

const CONTENT_BORDER_COLOR  = "#444444";
const CONTENT_BORDER_STYLE  =
  `${BORDER_WIDTH}px solid ${CONTENT_BORDER_COLOR}`;

const CONTENT_PADDING       = `10px`;
